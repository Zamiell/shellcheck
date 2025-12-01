# ShellCheck Rules Reference

This pages lists all 205 ShellCheck rules. (It was generated from the `src/ShellCheck/Analytics.hs` file.)

Rules with a long name are optional checks that can be enabled with `-o` or `enable` directives.

| SC Code | Long Name | Description/Message |
|---------|-----------|---------------------|
| SC2000 |  | See if you can use ${#variable} instead. |
| SC2002 | useless-use-of-cat | Check for Useless Use Of Cat (UUOC) |
| SC2004 |  | $/${} is unnecessary on arithmetic variables. |
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
| SC2025 |  | Make sure all escape sequences are enclosed in \\[..\\] to prevent line wrapping issues |
| SC2026 |  | This word is outside of quotes. Did you intend to 'nest '\ |
| SC2027 |  | The surrounding quotes actually unquote this. Remove or escape them. |
| SC2030 |  | Modification of  |
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
| SC2087 |  | Quote ' |
| SC2088 |  | Tilde does not expand in quotes. Use $HOME. |
| SC2091 |  | Remove surrounding $() to avoid executing output (or use eval if intentional). |
| SC2092 |  | Remove backticks to avoid executing output (or use eval if intentional). |
| SC2093 |  | Remove \ |
| SC2095 |  |  may swallow stdin, preventing this loop from working properly. |
| SC2097 |  | This assignment is only seen by the forked process. |
| SC2098 |  | This expansion will not see the mentioned assignment. |
| SC2099 |  | Use $((..)) for arithmetics, e.g. i=$((i  |
| SC2100 |  | Use $((..)) for arithmetics, e.g. i=$((i  |
| SC2101 |  | Named class needs outer [], e.g. [[:digit:]]. |
| SC2102 |  | Ranges can only match single chars (mentioned due to duplicates). |
| SC2103 |  | Use a ( subshell ) to avoid having to cd back. |
| SC2104 |  | In functions, use return instead of  |
| SC2106 |  | This only exits the subshell caused by the  |
| SC2107 |  | Instead of [ a && b ], use [ a ] && [ b ]. |
| SC2108 |  | In [[..]], use && instead of -a. |
| SC2109 |  | Instead of [ a \|\| b ], use [ a ] \|\| [ b ]. |
| SC2110 |  | In [[..]], use \|\| instead of -o. |
| SC2111 |  | ksh does not allow 'function' keyword and '()' at the same time. |
| SC2112 |  | 'function' keyword is non-standard. Delete it. |
| SC2113 |  | 'function' keyword is non-standard. Use 'foo()' instead of 'function foo'. |
| SC2116 |  | Useless echo? Instead of 'cmd $(echo foo)', just use 'cmd foo'. |
| SC2118 |  | Ksh does not support \|&. Use 2>&1 \|. |
| SC2119 |  | Use  |
| SC2120 |  |  references arguments, but none are ever passed. |
| SC2123 |  | PATH is the shell search path. Use another name. |
| SC2124 |  | Assigning an array to a string! Assign as array, or use * instead of @ to concatenate. |
| SC2125 |  | Brace expansions and globs are literal in assignments. Quote it or use an array. |
| SC2126 |  | Consider using 'grep -c' instead of 'grep\|wc -l'. |
| SC2127 |  | To use  |
| SC2129 |  | Consider using { cmd1; cmd2; } >> file instead of individual redirects. |
| SC2140 |  | Word is of the form \ |
| SC2141 |  | This backslash is literal. Did you mean IFS= |
| SC2143 |  | Use  |
| SC2144 |  |  doesn't work with globs. Use a for loop. |
| SC2145 |  | Argument mixes string and array. Use * or separate argument. |
| SC2147 |  | Literal tilde in PATH works poorly across programs. |
| SC2148 |  | Tips depend on target shell and yours is unknown. Add a shebang or a 'shell' directive. |
| SC2153 | check-unassigned-uppercase | Warn when uppercase variables are unassigned |
| SC2154 | check-unassigned-uppercase | Warn when uppercase variables are unassigned |
| SC2158 |  | [ false ] is true. Remove the brackets. |
| SC2159 |  | [ 0 ] is true. Use 'false' instead. |
| SC2160 |  | Instead of '[ true ]', just use 'true'. |
| SC2161 |  | Instead of '[ 1 ]', use 'true'. |
| SC2162 |  | read without -r will mangle backslashes. |
| SC2165 |  | This nested loop overrides the index variable of its parent. |
| SC2166 |  | Prefer [ p ] && [ q ] as [ p -a q ] is not well defined. |
| SC2167 |  | This parent loop has its index variable overridden. |
| SC2170 |  | Invalid number for  |
| SC2171 |  | Found trailing  |
| SC2181 |  | Check exit code directly with e.g. 'if  |
| SC2187 |  | Ash scripts will be checked as Dash. Add '# shellcheck shell=dash' to silence. |
| SC2188 |  | This redirection doesn't have a command. Move to its command (or use 'true' as no-op). |
| SC2189 |  | You can't have \| between this redirection and the command it should apply to. |
| SC2190 |  | Elements in associative arrays need index, e.g. array=( [index]=value ) . |
| SC2192 |  | This array element has no value. Remove spaces after = or use \ |
| SC2193 |  | The arguments to this comparison can never be equal. Make sure your syntax is correct. |
| SC2194 |  | This word is constant. Did you forget the $ on a variable? |
| SC2195 |  | This pattern will never match the case statement's word. Double check them. |
| SC2198 |  | Arrays don't work as operands in [ ]. Use a loop (or concatenate with * instead of @). |
| SC2199 |  | Arrays implicitly concatenate in [[ ]]. Use a loop (or explicit * instead of @). |
| SC2200 |  | Brace expansions don't work as operands in [ ]. Use a loop. |
| SC2201 |  | Brace expansion doesn't happen in [[ ]]. Use a loop. |
| SC2202 |  | Globs don't work as operands in [ ]. Use a loop. |
| SC2203 |  | Globs are ignored in [[ ]] except right of =/!=. Use a loop. |
| SC2204 |  | (..) is a subshell. Did you mean [ .. ], a test expression? |
| SC2205 |  | (..) is a subshell. Did you mean [ .. ], a test expression? |
| SC2208 |  | Use [[ ]] or quote arguments to -v to avoid glob expansion. |
| SC2209 |  | Use var=$(command) to assign output (or quote to assign string). |
| SC2210 |  | This is a file redirection. Was it supposed to be a comparison or fd operation? |
| SC2211 |  | This is a glob used as a command name. Was it supposed to be in ${..}, array, or is it missing quoting? |
| SC2212 |  | Use 'false' instead of empty [/[[ conditionals. |
| SC2215 |  | This flag is used as a command name. Bad line break or missing [ .. ]? |
| SC2216 |  | Piping to ' |
| SC2217 |  | Redirecting to ' |
| SC2218 |  | This function is only defined later. Move the definition up. |
| SC2221 |  | This pattern always overrides a later one |
| SC2222 |  | This pattern never matches because of a previous pattern |
| SC2223 | quote-safe-variables | Suggest quoting variables without metacharacters |
| SC2231 |  | Quote expansions in this for loop glob to prevent wordsplitting, e.g. \ |
| SC2233 |  | Remove superfluous (..) around condition to avoid subshell overhead. |
| SC2234 |  | Remove superfluous (..) around test command to avoid subshell overhead. |
| SC2235 |  | Use { ..; } instead of (..) to avoid subshell overhead. |
| SC2236 | avoid-negated-conditions | Suggest removing unnecessary comparison negations |
| SC2237 | avoid-negated-conditions | Suggest removing unnecessary comparison negations |
| SC2238 |  | Redirecting to/from command name instead of file. Did you want pipes/xargs (or quote to ignore)? |
| SC2239 |  | Ensure the shebang uses an absolute path to the interpreter. |
| SC2243 | avoid-nullary-conditions | Suggest explicitly using -n in `[ $var ]` |
| SC2244 | avoid-nullary-conditions | Suggest explicitly using -n in `[ $var ]` |
| SC2245 |  |  only applies to the first expansion of this glob. Use a loop to check any/all. |
| SC2246 |  | This shebang specifies a directory. Ensure the interpreter is a file. |
| SC2248 | quote-safe-variables | Suggest quoting variables without metacharacters |
| SC2249 | add-default-case | Suggest adding a default case in `case` statements |
| SC2250 | require-variable-braces | Suggest putting braces around all variable references |
| SC2252 |  | You probably wanted && here, otherwise it's always true. |
| SC2254 |  | Quote expansions in case patterns to match literally rather than as a glob. |
| SC2255 |  | [ ] does not apply arithmetic evaluation. Evaluate with $((..)) for numbers, or use string comparator for strings. |
| SC2257 |  | Arithmetic modifications in command redirections may be discarded. Do them separately. |
| SC2259 |  | This redirection overrides piped input. To use both, merge or pass filenames. |
| SC2260 |  | This redirection overrides the output pipe. Use 'tee' to output to both. |
| SC2261 |  | Multiple redirections compete for  |
| SC2262 |  | This alias can't be defined and used in the same parsing unit. Use a function instead. |
| SC2263 |  | Since they're in the same parsing unit, this command will not refer to the previously mentioned alias. |
| SC2269 |  | This variable is assigned to itself, so the assignment does nothing. |
| SC2270 |  | To assign positional parameters, use 'set -- first second ..' (or use [ ] to compare). |
| SC2271 |  | For indirection, use arrays, declare \ |
| SC2272 |  | Command name contains ==. For comparison, use [ \ |
| SC2273 |  | Sequence of ===s found. Merge conflict or intended as a commented border? |
| SC2274 |  | Command name starts with ===. Intended as a commented border? |
| SC2275 |  | Command name starts with =. Bad line break? |
| SC2276 |  | This is interpreted as a command name containing '='. Bad assignment or comparison? |
| SC2278 |  | $0 can't be assigned in Ksh (but it does reflect the current function). |
| SC2279 |  | $0 can't be assigned in Dash. This becomes a command name. |
| SC2280 |  | $0 can't be assigned this way, and there is no portable alternative. |
| SC2282 |  | Variable names can't start with numbers, so this is interpreted as a command. |
| SC2283 |  | Remove spaces around = to assign (or use [ ] to compare, or quote '=' if literal). |
| SC2284 |  | Use [ x = y ] to compare values (or quote '==' if literal). |
| SC2285 |  | Remove spaces around += to assign (or quote '+=' if literal). |
| SC2286 |  | This empty string is interpreted as a command name. Double check syntax (or use 'true' as a no-op). |
| SC2287 |  | This is interpreted as a command name ending with '/'. Double check syntax. |
| SC2288 |  | This is interpreted as a command name ending with  |
| SC2289 |  | This is interpreted as a command name containing a tab. Double check syntax. |
| SC2292 | require-double-brackets | Require [[ and warn about [ in Bash/Ksh |
| SC2296 |  | Parameter expansions can't start with  |
| SC2297 |  | Double quotes must be outside ${}: ${\ |
| SC2299 |  | Parameter expansions can't be nested. Use temporary variables. |
| SC2300 |  | Parameter expansion can't be applied to command substitutions. Use temporary variables. |
| SC2301 |  | Parameter expansion starts with unexpected  |
| SC2309 |  |  treats this as  |
| SC2310 | check-set-e-suppressed | Notify when set -e is suppressed during function invocation |
| SC2311 | check-set-e-suppressed | Notify when set -e is suppressed during function invocation |
| SC2312 | check-extra-masked-returns | Check for additional cases where exit codes are masked |
| SC2314 |  | In Bats, ! will not fail the test if it is not the last command anymore. Use `run ! ` (on Bats >= 1.5.0) instead. |
| SC2315 |  | In Bats, ! will not fail the test if it is not the last command anymore. Fold the `!` into the conditional! |
| SC2317 |  | Command appears to be unreachable. Check usage (or ignore if invoked indirectly). |
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
