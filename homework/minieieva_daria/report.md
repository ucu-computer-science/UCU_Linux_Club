### Week 6 Regular Expressions Homework

### This is a template for the report of 21 problems on [this site](http://regextutorials.com/excercise.html).

### Fork this repository, change this file and send us the link for grading.

### We recommend you (re)watch our presentation, and use a [cheatsheet](./cheatsheet.md) while working on the following problems.

### If you are having problems with figuring out the correct solution, skip it for later, and if you are completely lost, use the hints and try to understand them.

---

### Problem 1: Floating point numbers
```
\d\.\d+
```
### Problem 2: Years before 1990
```
\d\s\w*\s\w*[,|:]*(\s\w*)*\(1[0-9][0-8][0-9]\)
```
### Problem 3: Hexadecimal colors
```
#([A-Z]|[0-9]){6}
```
### Problem 4: Grayscale colors
```
#((([A-z]|[0-9]){1,2})\2{2})
```
### Problem 5: Too long lines
```
.{30,}
```
### Problem 6: Remove repeating words
```
(["]*\w+[-']*\w*)[\s.",]\1[\s.",]
$1 
```
### Problem 7: Match HTML tags
```
<[!/]*\w*\s*\w*>
```
### Problem 8: Cut numbers two digits after floating point
```
(\d\.\d{2})\d*
```
### Problem 9: Digit commas formatting
```
insert your pattern here
```
### Problem 10: Match lowercase function declarations
```
function+\s[a-z]\w*\(\w*\)
```
### Problem 11: Change date formats
```
(\d{4})-(\d{2})-(\d{2})
$3.$2.$1
```
### Problem 12: Validate 24h time format
```
([0-1][0-9]:[0-5][0-9])|([2][0-3]:[0-5][0-9])
```
### Problem 13: Validate AM/PM time format
```
((\s[0-9]?:[0-5][0-9])|([0-1][0-2]:[0-5][0-9]))\s([A|P]M)
```
### Problem 14: Pascal style to C-style parameters
```
(?<=[xyl]);
,
```
### Problem 15: Change variable initialization
```
var\s*(\w*)\s=\snew\s(.\w*<*\w*\>*)(.*;)
$2 $1$3
```
### Problem 16: IPv6 adresses
```
insert your pattern here
```
### Problem 17: Validate 32 or 24 bit hexadecimal colors
```
#(([0-9]|[fc])([0-9]|[fc])){3,4}(?=[\s,])
```
### Problem 18: Replace operators with function calls
```
insert your pattern here
```
### Problem 19: Extract query string from URL
```
\?.*
```
### Problem 20: Extract host from URL
```
http://w*\.?\w+\.com
```
### Problem 21: Strings not containing word
```
insert your pattern here
```
