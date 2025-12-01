# ShellCheck Rules Reference

This pages lists all 459 ShellCheck rules. (It was generated from the `src/ShellCheck/Analytics.hs`, `src/ShellCheck/Parser.hs`, and `src/ShellCheck/Checks/ShellSupport.hs` files.)

Rules with a long name are optional checks that can be enabled with `-o` or `enable` directives.

| SC Code | Long Name | Description/Message |
|---------|-----------|---------------------|
| SC1001 |  | This \\ |
| SC1003 |  | Want to escape a single quote? echo 'This is how it'\\''s done'. |
| SC1008 |  | This shebang was unrecognized. ShellCheck only supports sh/bash/dash/ksh/'busybox sh'. Add a 'shell' directive to specify. |
| SC1009 |  | The mentioned syntax error was in this  |
| SC1010 |  | Use semicolon or linefeed before ' |
| SC1011 |  | This apostrophe terminated the single quoted string! |
| SC1012 |  | \\ |
| SC1014 |  | Use 'if cmd; then ..' to check exit code, or 'if [[ $(cmd) == .. ]]' to check output. |
| SC1017 |  | Literal carriage return. Run script through tr -d '\\r' . |
| SC1018 |  | This is a unicode space. Delete and retype it. |
| SC1019 |  | Expected this to be an argument to the unary condition. |
| SC1020 |  | You need a space before the  |
| SC1021 |  | You need a space before the \\) |
| SC1026 |  | If grouping expressions inside [..], use \\( ..\\). |
| SC1027 |  | Expected another argument for this operator. |
| SC1028 |  | In [..] you have to escape \\( \\) or preferably combine [..] expressions. |
| SC1029 |  | In [[..]] you shouldn't escape ( or ). |
| SC1033 |  | Test expression was opened with double [[ but closed with single ]. Make sure they match. |
| SC1034 |  | Test expression was opened with single [ but closed with double ]]. Make sure they match. |
| SC1035 |  | You are missing a required space here. |
| SC1036 |  | '(' is invalid here. Did you forget to escape it? |
| SC1037 |  | Braces are required for positionals over 9, e.g. ${10}. |
| SC1039 |  | Remove indentation before end token (or use <<- and indent with tabs). |
| SC1040 |  | When using <<-, you can only indent with tabs. |
| SC1045 |  | It's not 'foo &; bar', just 'foo & bar'. |
| SC1046 |  | Couldn't find 'fi' for this 'if'. |
| SC1047 |  | Expected 'fi' matching previously mentioned 'if'. |
| SC1048 |  | Can't have empty  |
| SC1049 |  | Did you forget the 'then' for this 'if'? |
| SC1050 |  | Expected 'then'. |
| SC1054 |  | You need a space after the '{'. |
| SC1055 |  | You need at least one command here. Use 'true;' as a no-op. |
| SC1056 |  | Expected a '}'. If you have one, try a ; or \\n in front of it. |
| SC1057 |  | Did you forget the 'do' for this loop? |
| SC1058 |  | Expected 'do'. |
| SC1062 |  | Expected 'done' matching previously mentioned 'do'. |
| SC1063 |  | You need a line feed or semicolon before the 'do'. |
| SC1064 |  | Expected a { to open the function definition. |
| SC1065 |  | Trying to declare parameters? Don't. Use () and refer to params as $1, $2.. |
| SC1070 |  | Parsing stopped here. Mismatched keywords or invalid parentheses? |
| SC1071 |  | ShellCheck only supports sh/bash/dash/ksh/'busybox sh' scripts. Sorry! |
| SC1073 |  | Couldn't parse this  |
| SC1074 |  | Did you forget the ;; after the previous case item? |
| SC1075 |  | Use 'elif' instead of 'else if' (or put 'if' on new line if nesting). |
| SC1076 |  | Trying to do math? Use e.g. [ $((i/2+7)) -ge 18 ]. |
| SC1077 |  | For command expansion, the tick should slant left (` vs ´). Use $(..) instead. |
| SC1078 |  | Did you forget to close this  |
| SC1079 |  | This is actually an end quote, but due to next char it looks suspect. |
| SC1080 |  | When breaking lines in [ ], you need \\ before the linefeed. |
| SC1081 |  | Scripts are case sensitive. Use ' |
| SC1082 |  | This file has a UTF-8 BOM. Remove it with: LC_CTYPE=C sed '1s/^...//' < yourscript . |
| SC1083 |  | This  |
| SC1084 |  | Use #!, not !#, for the shebang. |
| SC1085 |  | Did you forget to move the ;; after extending this case item? |
| SC1087 |  | Use braces when expanding arrays, e.g. ${array[idx]} (or ${var}[.. to quiet). |
| SC1088 |  | Parsing stopped here. Invalid use of parentheses? |
| SC1089 |  | Parsing stopped here. Is this keyword correctly matched up? |
| SC1090 |  | ShellCheck can't follow non-constant source. Use a directive to specify location. |
| SC1091 |  | Not following:  |
| SC1092 |  | Stopping at 100 'source' frames :O |
| SC1093 |  | This file appears to be recursively sourced. Ignoring. |
| SC1094 |  | Parsing of sourced file failed. Ignoring it. |
| SC1097 |  | Unexpected ==. For assignment, use =. For comparison, use [/[[. Or quote for literal string. |
| SC1098 |  | Quote/escape special characters when using eval, e.g. eval \ |
| SC1100 |  | This is a unicode dash. Delete and retype as ASCII minus. |
| SC1101 |  | Delete trailing spaces after \\ to break line (or use quotes for literal space). |
| SC1102 |  | Shells disambiguate $(( differently or not at all. For $(command substitution), add space after $( . For $((arithmetics)), fix parsing errors. |
| SC1103 |  | This shell type is unknown. Use e.g. sh or bash. |
| SC1104 |  | Use #!, not just !, for the shebang. |
| SC1105 |  | Shells disambiguate (( differently or not at all. For subshell, add spaces around ( . For ((, fix parsing errors. |
| SC1106 |  | In arithmetic contexts, use  |
| SC1107 |  | This directive is unknown. It will be ignored. |
| SC1108 |  | You need a space before and after the  |
| SC1109 |  | This is an unquoted HTML entity. Replace with corresponding character. |
| SC1110 |  | This is a unicode quote. Delete and retype it (or quote to make literal). |
| SC1111 |  | This is a unicode quote. Delete and retype it (or ignore/singlequote for literal). |
| SC1112 |  | This is a unicode quote. Delete and retype it (or ignore/doublequote for literal). |
| SC1113 |  | Use #!, not just #, for the shebang. |
| SC1114 |  | Remove leading spaces before the shebang. |
| SC1115 |  | Remove spaces between # and ! in the shebang. |
| SC1116 |  | Missing $ on a $((..)) expression? (or use ( ( for arrays). |
| SC1118 |  | Delete whitespace after the here-doc end token. |
| SC1123 |  | ShellCheck directives are only valid in front of complete compound commands, like 'if', not e.g. individual 'elif' branches. |
| SC1124 |  | ShellCheck directives are only valid in front of complete commands like 'case' statements, not individual case branches. |
| SC1125 |  | Invalid key=value pair? Ignoring the rest of this directive starting here. |
| SC1126 |  | Place shellcheck directives before commands, not after. |
| SC1127 |  | Was this intended as a comment? Use # in sh. |
| SC1128 |  | The shebang must be on the first line. Delete blanks and move comments. |
| SC1132 |  | This & terminates the command. Escape it or add space after & to silence. |
| SC1133 |  | Unexpected start of line. If breaking lines, \|/\|\|/&& should be at the end of the previous one. |
| SC1134 |  | line  |
| SC1135 |  | Prefer escape over ending quote to make $ literal. Instead of \ |
| SC1142 |  | Use 'done < <(cmd)' to redirect from process substitution (currently missing one '<'). |
| SC1143 |  | This backslash is part of a comment and does not continue the line. |
| SC1144 |  | external-sources can only be enabled in .shellcheckrc, not in individual files. |
| SC1145 |  | Unknown external-sources value. Expected true/false. |
| SC1146 |  | Unknown extended-analysis value. Expected true/false. |
| SC2000 |  | See if you can use ${#variable} instead. |
| SC2002 | useless-use-of-cat | Check for Useless Use Of Cat (UUOC) |
| SC2003 |  | expr is antiquated. Consider rewriting this using $((..)), ${} or [[ ]]. |
| SC2004 |  | $/${} is unnecessary on arithmetic variables. |
| SC2005 |  | Useless echo? Instead of 'echo $(cmd)', just use 'cmd'. |
| SC2006 |  | Use $(...) notation instead of legacy backticks `...`. |
| SC2007 |  | Use $((..)) instead of deprecated $[..] |
| SC2009 |  | Consider using pgrep instead of grepping ps output. |
| SC2010 |  | Don't use ls \| grep. Use a glob or a for loop with a condition to allow non-alphanumeric filenames. |
| SC2011 |  | Use 'find .. -print0 \| xargs -0 ..' or 'find .. -exec .. +' to allow non-alphanumeric filenames. |
| SC2012 |  | Use find instead of ls to better handle non-alphanumeric filenames. |
| SC2013 |  | To read lines rather than words, pipe/redirect to a 'while read' loop. |
| SC2014 |  | This will expand once before find runs, not per file found. |
| SC2015 |  | Note that A && B \|\| C is not if-then-else. C may run when A is true. |
| SC2016 |  | Expressions don't expand in single quotes, use double quotes for that. |
| SC2017 |  | Increase precision by replacing a/b*c with a*c/b. |
| SC2018 |  | Use '[:lower:]' to support accents and foreign alphabets. |
| SC2019 |  | Use '[:upper:]' to support accents and foreign alphabets. |
| SC2020 |  | tr replaces sets of chars, not words (mentioned due to duplicates). |
| SC2021 |  | Don't use [] around classes in tr, it replaces literal square brackets. |
| SC2022 |  | Note that unlike globs,  |
| SC2023 |  | The shell may override 'time' as seen in man time(1). Use 'command time ..' for that one. |
| SC2024 |  | sudo doesn't affect redirects. Use sudo cat file \| .. |
| SC2025 |  | Make sure all escape sequences are enclosed in \\[..\\] to prevent line wrapping issues |
| SC2026 |  | This word is outside of quotes. Did you intend to 'nest '\ |
| SC2027 |  | The surrounding quotes actually unquote this. Remove or escape them. |
| SC2028 |  | echo may not expand escape sequences. Use printf. |
| SC2029 |  | Note that, unescaped, this expands on the client side. |
| SC2030 |  | Modification of  |
| SC2031 |  |  was modified in a subshell. That change might be lost. |
| SC2032 |  | This function can't be invoked via  |
| SC2033 |  | Shell functions can't be passed to external commands. Use separate script or sh -c. |
| SC2034 |  |  appears unused. Verify use (or export if used externally). |
| SC2035 |  | Use ./*glob* or -- *glob* so names with dashes won't become options. |
| SC2036 |  | If you wanted to assign the output of the pipeline, use a=$(b \| c) . |
| SC2037 |  | To assign the output of a command, use var=$(cmd) . |
| SC2038 |  | Use 'find .. -print0 \| xargs -0 ..' or 'find .. -exec .. +' to allow non-alphanumeric filenames. |
| SC2041 |  | This is a literal string. To run as a command, use $(..) instead of '..' .  |
| SC2042 |  | Use spaces, not commas, to separate loop elements. |
| SC2043 |  | This loop will only ever run once. Bad quoting or missing glob/expansion? |
| SC2044 |  | For loops over find output are fragile. Use find -exec or a while read loop. |
| SC2045 |  | Iterating over ls output is fragile. Use globs. |
| SC2046 |  | Quote this to prevent word splitting. |
| SC2048 |  | Use \ |
| SC2049 |  | =~ is for regex, but this looks like a glob. Use = instead. |
| SC2050 |  | This expression is constant. Did you forget the $ on a variable? |
| SC2053 |  | Quote the right-hand side of  |
| SC2054 |  | Use spaces, not commas, to separate array elements. |
| SC2055 |  | You probably wanted  |
| SC2056 |  | You probably wanted && here, otherwise it's always true. |
| SC2057 |  | Unknown binary operator. |
| SC2058 |  | Unknown unary operator. |
| SC2059 |  | Don't use variables in the printf format string. Use printf '..%s..' \ |
| SC2060 |  | Quote parameters to tr to prevent glob expansion. |
| SC2061 |  | Quote the parameter to  |
| SC2062 |  | Quote the grep pattern so the shell won't interpret it. |
| SC2063 |  | Grep uses regex, but this looks like a glob. |
| SC2064 |  | Use single quotes, otherwise this expands now rather than when signalled. |
| SC2065 |  | This is interpreted as a shell file redirection, not a comparison. |
| SC2066 |  | Since you double quoted this, it will not word split, and the loop will only run once. |
| SC2067 |  | Missing ';' or + terminating -exec. You can't use \|/\|\|/&&, and ';' has to be a separate, quoted argument. |
| SC2068 |  | Double quote array expansions to avoid re-splitting elements. |
| SC2069 |  | To redirect stdout+stderr, 2>&1 must be last (or use '{ cmd > file; } 2>&1' to clarify). |
| SC2070 |  | -n doesn't work with unquoted arguments. Quote or use [[ ]]. |
| SC2071 |  |  is for string comparisons. Use  |
| SC2073 |  | Escape \\ |
| SC2074 |  | Can't use =~ in [ ]. Use [[..]] instead. |
| SC2075 |  | Escaping  |
| SC2076 |  | Remove quotes from right-hand side of =~ to match as a regex rather than literally. |
| SC2077 |  | You need spaces around the comparison operator. |
| SC2078 |  | This expression is constant. Did you forget a $ somewhere? |
| SC2079 |  | (( )) doesn't support decimals. Use bc or awk. |
| SC2080 |  | Numbers with leading 0 are considered octal. |
| SC2082 |  | To expand via indirection, use arrays, ${!name} or (for sh only) eval. |
| SC2083 |  | Don't add spaces after the slash in './file'. |
| SC2084 |  | Remove '$' or use '_=$((expr))' to avoid executing output. |
| SC2086 |  | Double quote to prevent globbing and word splitting. |
| SC2087 |  | Quote ' |
| SC2088 |  | Tilde does not expand in quotes. Use $HOME. |
| SC2089 |  | Quotes/backslashes will be treated literally.  |
| SC2090 |  | Quotes/backslashes in this variable will not be respected. |
| SC2091 |  | Remove surrounding $() to avoid executing output (or use eval if intentional). |
| SC2092 |  | Remove backticks to avoid executing output (or use eval if intentional). |
| SC2093 |  | Remove \ |
| SC2094 |  | Make sure not to read and write the same file in the same pipeline. |
| SC2095 |  | Use  |
| SC2096 |  | On most OS, shebangs can only specify a single parameter. |
| SC2097 |  | This assignment is only seen by the forked process. |
| SC2098 |  | This expansion will not see the mentioned assignment. |
| SC2099 |  | Use $((..)) for arithmetics, e.g. i=$((i  |
| SC2100 |  | Use $((..)) for arithmetics, e.g. i=$((i  |
| SC2101 |  | Named class needs outer [], e.g. [[:digit:]]. |
| SC2102 |  | Ranges can only match single chars (mentioned due to duplicates). |
| SC2103 |  | Use a ( subshell ) to avoid having to cd back. |
| SC2104 |  | In functions, use return instead of  |
| SC2105 |  |  is only valid in loops. |
| SC2106 |  | This only exits the subshell caused by the  |
| SC2107 |  | Instead of [ a && b ], use [ a ] && [ b ]. |
| SC2108 |  | In [[..]], use && instead of -a. |
| SC2109 |  | Instead of [ a \|\| b ], use [ a ] \|\| [ b ]. |
| SC2110 |  | In [[..]], use \|\| instead of -o. |
| SC2111 |  | ksh does not allow 'function' keyword and '()' at the same time. |
| SC2112 |  | 'function' keyword is non-standard. Delete it. |
| SC2113 |  | 'function' keyword is non-standard. Use 'foo()' instead of 'function foo'. |
| SC2114 |  | Warning: deletes a system directory. |
| SC2115 |  | Use \ |
| SC2116 |  | Useless echo? Instead of 'cmd $(echo foo)', just use 'cmd foo'. |
| SC2117 |  | To run commands as another user, use su -c or sudo. |
| SC2118 |  | Ksh does not support \|&. Use 2>&1 \|. |
| SC2119 |  | Use  |
| SC2120 |  |  references arguments, but none are ever passed. |
| SC2121 |  | To assign a variable, use just 'var=value', no 'set ..'. |
| SC2122 |  |  is not a valid operator.  |
| SC2123 |  | PATH is the shell search path. Use another name. |
| SC2124 |  | Assigning an array to a string! Assign as array, or use * instead of @ to concatenate. |
| SC2125 |  | Brace expansions and globs are literal in assignments. Quote it or use an array. |
| SC2126 |  | Consider using 'grep -c' instead of 'grep\|wc -l'. |
| SC2127 |  | To use  |
| SC2128 |  | Expanding an array without an index only gives the first element. |
| SC2129 |  | Consider using { cmd1; cmd2; } >> file instead of individual redirects. |
| SC2139 |  | This expands when defined, not when used. Consider escaping. |
| SC2140 |  | Word is of the form \ |
| SC2141 |  | This backslash is literal. Did you mean IFS= |
| SC2142 |  | Aliases can't use positional parameters. Use a function. |
| SC2143 |  | Use  |
| SC2144 |  |  doesn't work with globs. Use a for loop. |
| SC2145 |  | Argument mixes string and array. Use * or separate argument. |
| SC2146 |  | This action ignores everything before the -o. Use \\( \\) to group. |
| SC2147 |  | Literal tilde in PATH works poorly across programs. |
| SC2148 |  | Tips depend on target shell and yours is unknown. Add a shebang or a 'shell' directive. |
| SC2150 |  | -exec does not invoke a shell. Rewrite or use -exec sh -c .. . |
| SC2151 |  | Only one integer 0-255 can be returned. Use stdout for other data. |
| SC2152 |  | Can only return 0-255. Other data should be written to stdout. |
| SC2153 | check-unassigned-uppercase | Warn when uppercase variables are unassigned |
| SC2154 | check-unassigned-uppercase | Warn when uppercase variables are unassigned |
| SC2155 |  | Declare and assign separately to avoid masking return values. |
| SC2156 |  | Injecting filenames is fragile and insecure. Use parameters. |
| SC2158 |  | [ false ] is true. Remove the brackets. |
| SC2159 |  | [ 0 ] is true. Use 'false' instead. |
| SC2160 |  | Instead of '[ true ]', just use 'true'. |
| SC2161 |  | Instead of '[ 1 ]', use 'true'. |
| SC2162 |  | read without -r will mangle backslashes. |
| SC2163 |  | This does not export ' |
| SC2164 |  | Use ' |
| SC2165 |  | This nested loop overrides the index variable of its parent. |
| SC2166 |  | Prefer [ p ] && [ q ] as [ p -a q ] is not well defined. |
| SC2167 |  | This parent loop has its index variable overridden. |
| SC2168 |  | 'local' is only valid in functions. |
| SC2170 |  | Invalid number for  |
| SC2171 |  | Found trailing  |
| SC2172 |  | Trapping signals by number is not well defined. Prefer signal names. |
| SC2173 |  | SIGKILL/SIGSTOP can not be trapped. |
| SC2174 |  | When used with -p, -m only applies to the deepest directory. |
| SC2176 |  | 'time' is undefined for pipelines. time single stage or bash -c instead. |
| SC2177 |  | 'time' is undefined for compound commands, time sh -c instead. |
| SC2178 |  | Variable was used as an array but is now assigned a string. |
| SC2179 |  | Use array+=(\ |
| SC2181 |  | Check exit code directly with e.g. 'if  |
| SC2182 |  | This printf format string has no variables. Other arguments are ignored. |
| SC2183 |  | This format string has  |
| SC2184 |  | Quote arguments to unset so they're not glob expanded. |
| SC2185 |  | Some finds don't have a default path. Specify '.' explicitly. |
| SC2186 |  | tempfile is deprecated. Use mktemp instead. |
| SC2187 |  | Ash scripts will be checked as Dash. Add '# shellcheck shell=dash' to silence. |
| SC2188 |  | This redirection doesn't have a command. Move to its command (or use 'true' as no-op). |
| SC2189 |  | You can't have \| between this redirection and the command it should apply to. |
| SC2190 |  | Elements in associative arrays need index, e.g. array=( [index]=value ) . |
| SC2191 |  | The = here is literal. To assign by index, use ( [index]=value ) with no spaces. To keep as literal, quote it. |
| SC2192 |  | This array element has no value. Remove spaces after = or use \ |
| SC2193 |  | The arguments to this comparison can never be equal. Make sure your syntax is correct. |
| SC2194 |  | This word is constant. Did you forget the $ on a variable? |
| SC2195 |  | This pattern will never match the case statement's word. Double check them. |
| SC2196 |  | egrep is non-standard and deprecated. Use grep -E instead. |
| SC2197 |  | fgrep is non-standard and deprecated. Use grep -F instead. |
| SC2198 |  | Arrays don't work as operands in [ ]. Use a loop (or concatenate with * instead of @). |
| SC2199 |  | Arrays implicitly concatenate in [[ ]]. Use a loop (or explicit * instead of @). |
| SC2200 |  | Brace expansions don't work as operands in [ ]. Use a loop. |
| SC2201 |  | Brace expansion doesn't happen in [[ ]]. Use a loop. |
| SC2202 |  | Globs don't work as operands in [ ]. Use a loop. |
| SC2203 |  | Globs are ignored in [[ ]] except right of =/!=. Use a loop. |
| SC2204 |  | (..) is a subshell. Did you mean [ .. ], a test expression? |
| SC2205 |  | (..) is a subshell. Did you mean [ .. ], a test expression? |
| SC2206 |  | Quote to prevent word splitting/globbing, or split robustly with read -A or while read. |
| SC2207 |  | Prefer read -A or while read to split command output (or quote to avoid splitting). |
| SC2208 |  | Use [[ ]] or quote arguments to -v to avoid glob expansion. |
| SC2209 |  | Use var=$(command) to assign output (or quote to assign string). |
| SC2210 |  | This is a file redirection. Was it supposed to be a comparison or fd operation? |
| SC2211 |  | This is a glob used as a command name. Was it supposed to be in ${..}, array, or is it missing quoting? |
| SC2212 |  | Use 'false' instead of empty [/[[ conditionals. |
| SC2213 |  | getopts specified - |
| SC2214 |  | This case is not specified by getopts. |
| SC2215 |  | This flag is used as a command name. Bad line break or missing [ .. ]? |
| SC2216 |  | Piping to ' |
| SC2217 |  | Redirecting to ' |
| SC2218 |  | This function is only defined later. Move the definition up. |
| SC2219 |  | Instead of 'let expr', prefer (( expr )) . |
| SC2220 |  | Invalid flags are not handled. Add a *) case. |
| SC2221 |  | This pattern always overrides a later one |
| SC2222 |  | This pattern never matches because of a previous pattern |
| SC2223 | quote-safe-variables | Suggest quoting variables without metacharacters |
| SC2224 |  | This mv has no destination. Check the arguments. |
| SC2225 |  | This cp has no destination. Check the arguments. |
| SC2226 |  | This ln has no destination. Check the arguments, or specify '.' explicitly. |
| SC2227 |  | Redirection applies to the find command itself. Rewrite to work per action (or move to end). |
| SC2229 |  | This does not read ' |
| SC2230 |  | 'which' is non-standard. Use builtin 'command -v' instead. |
| SC2231 |  | Quote expansions in this for loop glob to prevent wordsplitting, e.g. \ |
| SC2232 |  | Can't use sudo with builtins like  |
| SC2233 |  | Remove superfluous (..) around condition to avoid subshell overhead. |
| SC2234 |  | Remove superfluous (..) around test command to avoid subshell overhead. |
| SC2235 |  | Use { ..; } instead of (..) to avoid subshell overhead. |
| SC2236 | avoid-negated-conditions | Suggest removing unnecessary comparison negations |
| SC2237 | avoid-negated-conditions | Suggest removing unnecessary comparison negations |
| SC2238 |  | Redirecting to/from command name instead of file. Did you want pipes/xargs (or quote to ignore)? |
| SC2239 |  | Ensure the shebang uses an absolute path to the interpreter. |
| SC2240 |  | The dot command does not support arguments in sh/dash. Set them as variables. |
| SC2241 |  | The exit status can only be one integer 0-255. Use stdout for other data. |
| SC2242 |  | Can only exit with status 0-255. Other data should be written to stdout/stderr. |
| SC2243 | avoid-nullary-conditions | Suggest explicitly using -n in `[ $var ]` |
| SC2244 | avoid-nullary-conditions | Suggest explicitly using -n in `[ $var ]` |
| SC2245 |  |  only applies to the first expansion of this glob. Use a loop to check any/all. |
| SC2246 |  | This shebang specifies a directory. Ensure the interpreter is a file. |
| SC2247 |  | Flip leading $ and \ |
| SC2248 | quote-safe-variables | Suggest quoting variables without metacharacters |
| SC2249 | add-default-case | Suggest adding a default case in `case` statements |
| SC2250 | require-variable-braces | Suggest putting braces around all variable references |
| SC2251 |  | This ! is not on a condition and skips errexit. Use `&& exit 1` instead, or make sure $? is checked. |
| SC2252 |  | You probably wanted && here, otherwise it's always true. |
| SC2253 |  | Use -R to recurse, or explicitly a-r to remove read permissions. |
| SC2254 |  | Quote expansions in case patterns to match literally rather than as a glob. |
| SC2255 |  | [ ] does not apply arithmetic evaluation. Evaluate with $((..)) for numbers, or use string comparator for strings. |
| SC2256 |  | This translated string is the name of a variable. Flip leading $ and \ |
| SC2257 |  | Arithmetic modifications in command redirections may be discarded. Do them separately. |
| SC2258 |  | The trailing comma is part of the value, not a separator. Delete or quote it. |
| SC2259 |  | This redirection overrides piped input. To use both, merge or pass filenames. |
| SC2260 |  | This redirection overrides the output pipe. Use 'tee' to output to both. |
| SC2261 |  | Multiple redirections compete for  |
| SC2262 |  | This alias can't be defined and used in the same parsing unit. Use a function instead. |
| SC2263 |  | Since they're in the same parsing unit, this command will not refer to the previously mentioned alias. |
| SC2264 |  | This function unconditionally re-invokes itself. Missing 'command'? |
| SC2265 |  | Use && for logical AND. Single & will background and return true. |
| SC2266 |  | Use \|\| for logical OR. Single \| will pipe. |
| SC2267 |  | GNU xargs -i is deprecated in favor of -I{} |
| SC2269 |  | This variable is assigned to itself, so the assignment does nothing. |
| SC2270 |  | To assign positional parameters, use 'set -- first second ..' (or use [ ] to compare). |
| SC2271 |  | For indirection, use arrays, declare \ |
| SC2272 |  | Command name contains ==. For comparison, use [ \ |
| SC2273 |  | Sequence of ===s found. Merge conflict or intended as a commented border? |
| SC2274 |  | Command name starts with ===. Intended as a commented border? |
| SC2275 |  | Command name starts with =. Bad line break? |
| SC2276 |  | This is interpreted as a command name containing '='. Bad assignment or comparison? |
| SC2277 |  | Use BASH_ARGV0 to assign to $0 in bash (or use [ ] to compare). |
| SC2278 |  | $0 can't be assigned in Ksh (but it does reflect the current function). |
| SC2279 |  | $0 can't be assigned in Dash. This becomes a command name. |
| SC2280 |  | $0 can't be assigned this way, and there is no portable alternative. |
| SC2281 |  | Don't use  |
| SC2282 |  | Variable names can't start with numbers, so this is interpreted as a command. |
| SC2283 |  | Remove spaces around = to assign (or use [ ] to compare, or quote '=' if literal). |
| SC2284 |  | Use [ x = y ] to compare values (or quote '==' if literal). |
| SC2285 |  | Remove spaces around += to assign (or quote '+=' if literal). |
| SC2286 |  | This empty string is interpreted as a command name. Double check syntax (or use 'true' as a no-op). |
| SC2287 |  | This is interpreted as a command name ending with '/'. Double check syntax. |
| SC2288 |  | This is interpreted as a command name ending with  |
| SC2289 |  | This is interpreted as a command name containing a tab. Double check syntax. |
| SC2290 |  | Remove spaces around = to assign. |
| SC2291 |  | Quote repeated spaces to avoid them collapsing into one. |
| SC2292 | require-double-brackets | Require [[ and warn about [ in Bash/Ksh |
| SC2293 |  | When eval'ing @Q-quoted words, use * rather than @ as the index. |
| SC2294 |  | eval negates the benefit of arrays. Drop eval to preserve whitespace/symbols (or eval as string). |
| SC2295 |  | Expansions inside ${..} need to be quoted separately, otherwise they match as patterns. |
| SC2296 |  | Parameter expansions can't start with  |
| SC2297 |  | Double quotes must be outside ${}: ${\ |
| SC2298 |  | ${${x}} |
| SC2299 |  | Parameter expansions can't be nested. Use temporary variables. |
| SC2300 |  | Parameter expansion can't be applied to command substitutions. Use temporary variables. |
| SC2301 |  | Parameter expansion starts with unexpected  |
| SC2302 |  | This loops over values. To loop over keys, use \ |
| SC2304 |  | * must be escaped to multiply: \\*. Modern $((x * y)) avoids this issue. |
| SC2305 |  | Quote regex argument to expr to avoid it expanding as a glob. |
| SC2306 |  | Escape glob characters in arguments to expr to avoid pathname expansion. |
| SC2307 |  | 'expr' expects 3+ arguments but sees 1. Make sure each operator/operand is a separate argument, and escape <>&\|. |
| SC2309 |  |  treats this as  |
| SC2310 | check-set-e-suppressed | Notify when set -e is suppressed during function invocation |
| SC2311 | check-set-e-suppressed | Notify when set -e is suppressed during function invocation |
| SC2312 | check-extra-masked-returns | Check for additional cases where exit codes are masked |
| SC2313 |  | Quote array indices to avoid them expanding as globs. |
| SC2314 |  | In Bats, ! will not fail the test if it is not the last command anymore. Use `run ! ` (on Bats >= 1.5.0) instead. |
| SC2315 |  | In Bats, ! will not fail the test if it is not the last command anymore. Fold the `!` into the conditional! |
| SC2316 |  | This applies  |
| SC2317 |  | Command appears to be unreachable. Check usage (or ignore if invoked indirectly). |
| SC2318 |  | This assignment is used again in this ' |
| SC2319 |  | This $? refers to a condition, not a command. Assign to a variable to avoid it being overwritten. |
| SC2320 |  | This $? refers to echo/printf, not a previous command. Assign to variable to avoid it being overwritten. |
| SC2321 |  | Array indices are already arithmetic contexts. Prefer removing the $(( and )). |
| SC2322 |  | In arithmetic contexts, ((x)) is the same as (x). Prefer only one layer of parentheses. |
| SC2324 |  | var+=1 will append, not increment. Use (( var += 1 )), typeset -i var, or quote number to silence. |
| SC2327 |  | This command substitution will be empty because the command's output gets redirected away. |
| SC2328 |  | This redirection takes output away from the command substitution |
| SC2329 |  | This function is never invoked. Check usage (or ignored if invoked indirectly). |
| SC2330 |  | BusyBox [[ .. ]] does not support glob matching. Use a case statement. |
| SC2331 |  | For file existence, prefer standard -e over legacy -a. |
| SC2333 |  | You probably wanted \|\| here, otherwise it's always false. |
| SC2334 |  | You probably wanted \|\| here, otherwise it's always false. |
| SC2335 | avoid-negated-conditions | Suggest removing unnecessary comparison negations |
| SC2336 |  | cp -r behavior is implementation-defined |
| SC3001 |  | process substitution is |
| SC3002 |  | extglob is |
| SC3003 |  | $'..' is |
| SC3004 |  | $\ |
| SC3005 |  | arithmetic for loops are |
| SC3006 |  | standalone ((..)) is |
| SC3007 |  | $[..] in place of $((..)) is |
| SC3008 |  | select loops are |
| SC3009 |  | brace expansion is |
| SC3010 |  | [[ ]] is |
| SC3011 |  | here-strings are |
| SC3012 |  | lexicographical  |
| SC3014 |  |  in place of = is |
| SC3015 |  |  regex matching is |
| SC3016 |  | test  |
| SC3017 |  | unary  |
| SC3018 |  |  is |
| SC3019 |  | exponentials are |
| SC3020 |  | &> is |
| SC3021 |  | >& filename (as opposed to >& fd) is |
| SC3022 |  | named file descriptors are |
| SC3023 |  | FDs outside 0-9 are |
| SC3024 |  | += is |
| SC3025 |  | /dev/{tcp,udp} is |
| SC3026 |  | ^ in place of ! in glob bracket expressions is |
| SC3028 |  |  is |
| SC3029 |  | \|& in place of 2>&1 \| is |
| SC3030 |  | arrays are |
| SC3031 |  | redirecting to/from globs is |
| SC3032 |  | coproc is |
| SC3033 |  | naming functions outside [a-zA-Z_][a-zA-Z0-9_]* is |
| SC3034 |  | $(<file) to read files is |
| SC3035 |  | `<file` to read files is |
| SC3036 |  | echo flags besides -n and -e |
| SC3037 |  | echo flags are |
| SC3038 |  | exec flags are |
| SC3039 |  | 'let' is |
| SC3040 |  | set option  |
| SC3041 |  | set flag  |
| SC3042 |  | set flag  |
| SC3043 |  | 'local' is |
| SC3044 |  | ' |
| SC3045 |  |  - |
| SC3046 |  | 'source' in place of '.' is |
| SC3047 |  | trapping  |
| SC3048 |  | prefixing signal names with 'SIG' is |
| SC3049 |  | using lower/mixed case for signal names is |
| SC3050 |  | printf %q is |
| SC3051 |  | 'source' in place of '.' is |
| SC3052 |  | arithmetic base conversion is |
| SC3061 |  | read without a variable is |
| SC3062 |  | test  |
| SC3063 |  | test  |
| SC3064 |  | test  |
| SC3065 |  | test  |
| SC3066 |  | test  |
| SC3067 |  | test  |
