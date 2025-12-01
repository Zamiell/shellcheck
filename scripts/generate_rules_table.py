#!/usr/bin/env python3
"""
Generate a Markdown table of all ShellCheck rules with their SC codes and long names.
"""

import re
import sys
from pathlib import Path


def extract_optional_checks(content):
    """Extract optional check names and their associated function names."""
    checks = []

    # Find the optionalTreeChecks section
    optional_section = re.search(
        r'optionalTreeChecks :: .*?\noptionalTreeChecks = \[(.*?)\n    \]',
        content,
        re.DOTALL
    )

    if not optional_section:
        print("Warning: Could not find optionalTreeChecks section", file=sys.stderr)
        return checks

    # Parse each check description
    # Pattern to match: cdName = "...", followed by }, and then function reference
    pattern = r'cdName = "([^"]+)".*?cdDescription = "([^"]+)".*?\}, (?:nodeChecksToTreeCheck \[)?([a-zA-Z0-9_\']+)'

    for match in re.finditer(pattern, optional_section.group(1), re.DOTALL):
        long_name = match.group(1)
        description = match.group(2)
        function_name = match.group(3)
        checks.append({
            'long_name': long_name,
            'description': description,
            'function': function_name,
            'codes': []
        })

    return checks


def extract_sc_codes_from_function(content, function_name):
    """Extract all SC codes used in a function."""
    codes = []

    # First check if it's an alias to another function
    alias_pattern = rf'^{re.escape(function_name)}\s*=\s*([a-zA-Z0-9_\']+)'
    alias_match = re.search(alias_pattern, content, re.MULTILINE)
    if alias_match:
        # Recursively look up the aliased function
        aliased_func = alias_match.group(1)
        return extract_sc_codes_from_function(content, aliased_func)

    # Find the function definition
    # Look for patterns like:
    # - functionName _ t =
    # - functionName params t =
    # - functionName params t@(...) =
    # - functionName params t@(...)  (= on next line with guard)
    func_pattern = rf'^{re.escape(function_name)}\s+[^=\n]+'

    lines = content.split('\n')
    in_function = False
    indent_level = None
    function_start = -1

    for i, line in enumerate(lines):
        # Check if we're starting the function
        # Must have the function name at the start and some parameters
        if re.match(func_pattern, line):
            # Check if this line has = or if we should continue to next line
            if '=' in line or (i + 1 < len(lines) and lines[i + 1].strip().startswith('|')):
                in_function = True
                function_start = i
                indent_level = len(line) - len(line.lstrip())
                # Check this line for codes too
                codes.extend(extract_codes_from_line(line))
                continue

        if in_function:
            # Check if we've left the function
            current_indent = len(line) - len(line.lstrip())
            stripped = line.strip()

            # Stop if we hit another function definition at same or less indent
            if stripped and indent_level is not None and current_indent <= indent_level:
                # Check if this is a new top-level definition
                if re.match(r'^[a-z][a-zA-Z0-9_\']*\s+[^=]*=', stripped) or \
                   re.match(r'^prop_', stripped):
                    break

            # Extract codes from this line
            codes.extend(extract_codes_from_line(line))

    return list(set(codes))  # Remove duplicates


def extract_codes_from_line(line):
    """Extract SC codes from a single line."""
    codes = []
    # Pattern: (err|warn|info|style|styleWithFix) ... CODE ...
    # The code is always a 4-digit number, and typically appears as:
    # - err id 2107 "message"
    # - style id 2250 "message"
    # - styleWithFix id 2243 "message" fix
    # - style (getId word) 2002 "message"
    #
    # So the pattern is: style/err/warn/info/styleWithFix, then some stuff, then a 4-digit code
    # We need to match both: "style id 2250" and "style (getId word) 2002"
    code_pattern = r'\b(?:err|warn|info|style(?:WithFix)?)\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\b'
    for match in re.finditer(code_pattern, line):
        code = match.group(1)
        codes.append(f"SC{code}")
    return codes


def extract_all_sc_codes(content):
    """Extract all SC codes and their messages from Analytics.hs."""
    all_codes = {}

    # Pattern 1: (err|warn|info|style)[WithFix|type] id CODE "message" (on same line)
    pattern1 = r'(?:err|warn|info|style)(?:WithFix|type)?\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+"([^"]+)'
    for match in re.finditer(pattern1, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 2: (err|warn|info|style)[WithFix|type] id CODE $ (message on next line(s))
    # This handles cases like: info id 2153 $\n"message"
    pattern2 = r'(?:err|warn|info|style)(?:WithFix|type)?\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+(?:\$|[\(\{])\s*\n\s*"([^"]+)'
    for match in re.finditer(pattern2, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 3: For style messages with $: style id CODE $ "message"
    pattern3 = r'(?:err|warn|info|style)(?:WithFix|type)?\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+\$\s+"([^"]+)'
    for match in re.finditer(pattern3, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 4: For messages starting with paren: info id CODE ("message"
    pattern4 = r'(?:err|warn|info|style)(?:WithFix|type)?\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+\("([^"]+)'
    for match in re.finditer(pattern4, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 5: For messages with $ followed by string concat: warn id CODE $\nvar ++ "message"
    # This is complex, so let's just get the partial message
    pattern5 = r'(?:err|warn|info|style)(?:WithFix|type)?\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+\$\s*\n\s*\w+\s*\+\+\s*"([^"]+)'
    for match in re.finditer(pattern5, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)  # This will be partial but better than nothing
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 6: makeComment[WithFix] (ErrorC|WarningC|InfoC|StyleC) id CODE "message"
    pattern6 = r'makeComment(?:WithFix)?\s+(?:ErrorC|WarningC|InfoC|StyleC)\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+"([^"]+)'
    for match in re.finditer(pattern6, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 7: makeComment[WithFix] (ErrorC|WarningC|InfoC|StyleC) id CODE $\n"message"
    pattern7 = r'makeComment(?:WithFix)?\s+(?:ErrorC|WarningC|InfoC|StyleC)\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+\$\s*\n\s*"([^"]+)'
    for match in re.finditer(pattern7, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 8: Single-line variable concatenation: info id CODE $ var ++ "message"
    pattern8 = r'(?:err|warn|info|style)(?:WithFix|type)?\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+\$\s*\w+\s*\+\+\s*"([^"]+)'
    for match in re.finditer(pattern8, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 9: Complex expressions after $: CODE $ ... "message" (catches if/then/else, etc.)
    # This is a catch-all for patterns like: warn id CODE $\n    if ...\n    then "message"\n    else "other"
    pattern9 = r'(?:err|warn|info|style)(?:WithFix|type)?\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+\$[^"]*?"([^"]+)"'
    for match in re.finditer(pattern9, content, re.DOTALL):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    return all_codes


def extract_shellsupport_sc_codes(content):
    """Extract all SC codes and their messages from ShellSupport.hs."""
    all_codes = {}

    # Pattern 1: warnMsg id CODE "message" or warnMsg id CODE $ "message"
    pattern1 = r'warnMsg\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+"([^"]+)'
    for match in re.finditer(pattern1, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 2: warnMsg id CODE $\n"message"
    pattern2 = r'warnMsg\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+\$\s*\n\s*"([^"]+)'
    for match in re.finditer(pattern2, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 3: warnMsg id CODE $ var ++ "message" (single line concat)
    pattern3 = r'warnMsg\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+\$\s*\w+\s*\+\+\s*"([^"]+)'
    for match in re.finditer(pattern3, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 4: Tuple patterns like (CODE, [...], \x -> "message")
    pattern4 = r'\((\d{4}),.*?->.*?"([^"]+)"'
    for match in re.finditer(pattern4, content, re.DOTALL):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 5: Catch-all for warnMsg CODE $ ... "message"
    pattern5 = r'warnMsg\s+(?:\([^)]+\)|[\w\']+)\s+(\d{4})\s+\$[^"]*?"([^"]+)"'
    for match in re.finditer(pattern5, content, re.DOTALL):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    return all_codes


def extract_parser_sc_codes(content):
    """Extract all SC codes and their messages from Parser.hs."""
    all_codes = {}

    # Pattern 1: parseNote[At|AtId|AtWithEnd] [pos] (ErrorC|WarningC|InfoC) CODE "message" (on same line)
    pattern1 = r'parseNote(?:At(?:Id|WithEnd)?)?\s+(?:\w+\s+)?(?:ErrorC|WarningC|InfoC|StyleC)\s+(\d{4})\s+"([^"]+)'
    for match in re.finditer(pattern1, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 2: parseNote[At|AtId|AtWithEnd] [pos] (ErrorC|WarningC|InfoC) CODE $\n"message"
    pattern2 = r'parseNote(?:At(?:Id|WithEnd)?)?\s+(?:\w+\s+)?(?:ErrorC|WarningC|InfoC|StyleC)\s+(\d{4})\s+\$\s*\n\s*"([^"]+)'
    for match in re.finditer(pattern2, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 3: parseNote[At|AtId|AtWithEnd] [pos] (ErrorC|WarningC|InfoC) CODE $ "message"
    pattern3 = r'parseNote(?:At(?:Id|WithEnd)?)?\s+(?:\w+\s+)?(?:ErrorC|WarningC|InfoC|StyleC)\s+(\d{4})\s+\$\s+"([^"]+)'
    for match in re.finditer(pattern3, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 4: parseProblem[At|AtId|AtWithEnd] [pos] (ErrorC|WarningC|InfoC) CODE "message" (on same line)
    pattern4 = r'parseProblem(?:At(?:Id|WithEnd)?)?\s+(?:\w+\s+)?(?:ErrorC|WarningC|InfoC|StyleC)\s+(\d{4})\s+"([^"]+)'
    for match in re.finditer(pattern4, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 5: parseProblem[At|AtId|AtWithEnd] [pos] (ErrorC|WarningC|InfoC) CODE $\n"message"
    pattern5 = r'parseProblem(?:At(?:Id|WithEnd)?)?\s+(?:\w+\s+)?(?:ErrorC|WarningC|InfoC|StyleC)\s+(\d{4})\s+\$\s*\n\s*"([^"]+)'
    for match in re.finditer(pattern5, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 6: parseProblem[At|AtId|AtWithEnd] [pos] (ErrorC|WarningC|InfoC) CODE $ "message"
    pattern6 = r'parseProblem(?:At(?:Id|WithEnd)?)?\s+(?:\w+\s+)?(?:ErrorC|WarningC|InfoC|StyleC)\s+(\d{4})\s+\$\s+"([^"]+)'
    for match in re.finditer(pattern6, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 7: ParseNote constructor (capital P): ParseNote pos pos (ErrorC|WarningC|InfoC) CODE $
    pattern7 = r'ParseNote\s+\w+\s+\w+\s+(?:ErrorC|WarningC|InfoC|StyleC)\s+(\d{4})\s+\$\s*\n\s*"([^"]+)'
    for match in re.finditer(pattern7, content):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    # Pattern 8: Catch-all for parseProblem/parseNote CODE $ ... "message"
    pattern8 = r'(?:parseProblem|parseNote)(?:At(?:Id|WithEnd)?)?\s+(?:\w+\s+)?(?:ErrorC|WarningC|InfoC|StyleC)\s+(\d{4})\s+\$[^"]*?"([^"]+)"'
    for match in re.finditer(pattern8, content, re.DOTALL):
        code = f"SC{match.group(1)}"
        message = match.group(2)
        if code not in all_codes:
            all_codes[code] = message

    return all_codes


def main():
    # Read all the Haskell source files with SC codes
    project_root = Path(__file__).parent.parent
    analytics_path = project_root / 'src' / 'ShellCheck' / 'Analytics.hs'
    parser_path = project_root / 'src' / 'ShellCheck' / 'Parser.hs'
    shellsupport_path = project_root / 'src' / 'ShellCheck' / 'Checks' / 'ShellSupport.hs'
    commands_path = project_root / 'src' / 'ShellCheck' / 'Checks' / 'Commands.hs'
    controlflow_path = project_root / 'src' / 'ShellCheck' / 'Checks' / 'ControlFlow.hs'

    files_to_read = {
        'Analytics.hs': analytics_path,
        'Parser.hs': parser_path,
        'ShellSupport.hs': shellsupport_path,
        'Commands.hs': commands_path,
        'ControlFlow.hs': controlflow_path
    }

    for name, path in files_to_read.items():
        if not path.exists():
            print(f"Error: {path} not found", file=sys.stderr)
            sys.exit(1)

    analytics_content = analytics_path.read_text(encoding='utf-8')
    parser_content = parser_path.read_text(encoding='utf-8')
    shellsupport_content = shellsupport_path.read_text(encoding='utf-8')
    commands_content = commands_path.read_text(encoding='utf-8')
    controlflow_content = controlflow_path.read_text(encoding='utf-8')

    # Extract optional checks with their long names
    optional_checks = extract_optional_checks(analytics_content)

    print(f"Found {len(optional_checks)} optional checks", file=sys.stderr)

    # For each optional check, find its SC codes
    for check in optional_checks:
        check['codes'] = extract_sc_codes_from_function(analytics_content, check['function'])
        print(f"  {check['long_name']}: {check['function']} -> {check['codes']}", file=sys.stderr)

    # Extract all SC codes with their messages from all files
    all_codes = extract_all_sc_codes(analytics_content)
    parser_codes = extract_parser_sc_codes(parser_content)
    shellsupport_codes = extract_shellsupport_sc_codes(shellsupport_content)
    commands_codes = extract_all_sc_codes(commands_content)  # Uses same pattern as Analytics
    controlflow_codes = extract_all_sc_codes(controlflow_content)  # Uses same pattern as Analytics

    print(f"\nFound {len(all_codes)} SC codes in Analytics.hs", file=sys.stderr)
    print(f"Found {len(parser_codes)} SC codes in Parser.hs", file=sys.stderr)
    print(f"Found {len(shellsupport_codes)} SC codes in ShellSupport.hs", file=sys.stderr)
    print(f"Found {len(commands_codes)} SC codes in Commands.hs", file=sys.stderr)
    print(f"Found {len(controlflow_codes)} SC codes in ControlFlow.hs", file=sys.stderr)

    # Merge the codes (first file takes precedence if there are duplicates)
    all_codes.update({k: v for k, v in parser_codes.items() if k not in all_codes})
    all_codes.update({k: v for k, v in shellsupport_codes.items() if k not in all_codes})
    all_codes.update({k: v for k, v in commands_codes.items() if k not in all_codes})
    all_codes.update({k: v for k, v in controlflow_codes.items() if k not in all_codes})

    print(f"Total unique SC codes: {len(all_codes)}", file=sys.stderr)

    # Create mapping from SC code to long name
    code_to_check = {}
    for check in optional_checks:
        for code in check['codes']:
            code_to_check[code] = check

    # Generate Markdown table
    output = []
    output.append("# ShellCheck Rules Reference\n")
    analytics_rel = analytics_path.relative_to(project_root).as_posix()
    parser_rel = parser_path.relative_to(project_root).as_posix()
    shellsupport_rel = shellsupport_path.relative_to(project_root).as_posix()
    output.append(f"This pages lists all {len(all_codes)} ShellCheck rules. (It was generated from the `{analytics_rel}`, `{parser_rel}`, and `{shellsupport_rel}` files.)\n")
    output.append("Rules with a long name are optional checks that can be enabled with `-o` or `enable` directives.\n")
    output.append("| SC Code | Long Name | Description/Message |")
    output.append("|---------|-----------|---------------------|")

    # Sort by SC code
    for code in sorted(all_codes.keys(), key=lambda x: int(x[2:])):
        long_name = ""
        description = all_codes[code]

        if code in code_to_check:
            check = code_to_check[code]
            long_name = check['long_name']
            description = check['description']

        # Escape pipe characters in descriptions
        description = description.replace('|', '\\|')

        output.append(f"| {code} | {long_name} | {description} |")

    # Write to file
    markdown_path = project_root / "rules.md"
    markdown_path.write_text('\n'.join(output) + '\n', encoding='utf-8')

    print(f"\n✓ Generated {markdown_path}", file=sys.stderr)
    print(f"  Total rules: {len(all_codes)}", file=sys.stderr)
    print(f"  Optional rules with long names: {len([c for c in code_to_check.values()])}", file=sys.stderr)


if __name__ == '__main__':
    main()
