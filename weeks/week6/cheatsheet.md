### Anchors

* `^` - Start of string
* `$` - End of string
* `\b` - Word boundary
* `\B` - Not word boundary

### Assertions

* `?=` - Lookahead assertion
* `?!` - Negative lookahead
* `?<=` - Lookbehind assertion
* `?!=` - Negative lookbehind

### Groups and Ranges

* `.` - Any character except newline
* `(a|b)` - a or b
* `(...)` - Group
* `[abc]` - a or b or c
* `[^abc]` - Not (a or b or c)
* `[a-q]` - a or b or ... up to q
* `[A-Q]` - The same, but for uppercase letters
* `[2-7]` - The same, but for digits
* `\x` - Allows to reuse group number `x`

### Character classes

* `\s` - White space
* `\d` - Digit
* `\w` - Word
* `\S` `\D` `\W` - Not whitespace, digit or word respectively

### Quantifiers

* `*` - 0 or more
* `+` - 1 or more
* `?` - 0 or 1
* `{3}` - Exactly 3
* `{3,}` - 3 or more
* `{3,5}` - 3,4 or 5

### Escape sequences and common metacharacters

* `\` - Escape the following metacharacter
* `{}[]()^$.*+?|\` - Common metacharacters to escape to use their literal meaning

### String replacement

* `$n` - nth group
* `$1` - will capture first group - `abc` in `(abc)(xyz)`

