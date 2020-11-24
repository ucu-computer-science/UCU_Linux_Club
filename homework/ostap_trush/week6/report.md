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
.*\(19[1-8]\d\) - but I did not know it here
```
### Problem 3: Hexadecimal colors
```
#\w{6}
```
### Problem 4: Grayscale colors
```
no idea
```
### Problem 5: Too long lines
```
^(.){25,}$
```
### Problem 6: Remove repeating words
```
insert your pattern here
```
### Problem 7: Match HTML tags
```
<[!/]?\w+\s?\w*>
```
### Problem 8: Cut numbers two digits after floating point
```
(\d\.\d\d)\d+
$1
```
### Problem 9: Digit commas formatting
```
(\d)(?=(\d{3})+\b)
$1,
```
### Problem 10: Match lowercase function declarations
```
function [a-z]\w+.\w*.
```
### Problem 11: Change date formats
```
((\d{4})-(\d{2})-(\d{2}))
$4.$3.$2
```
### Problem 12: Validate 24h time format
```
[0-2][0-9]:[0-5][0-9] - a bit wrong but that is the best I could go
```
### Problem 13: Validate AM/PM time format
```
insert your pattern here
```
### Problem 14: Pascal style to C-style parameters
```
(\w);.
$1, (there is a space there)
```
### Problem 15: Change variable initialization
```
((\d|[a-f])(?![a-z]){1,4}) - the closest I got
```
### Problem 16: IPv6 adresses
```
insert your pattern here
```
### Problem 17: Validate 32 or 24 bit hexadecimal colors
```
#((0|f){6})((f|8){2})*(?!f)
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
http:.+com
```
### Problem 21: Strings not containing word
```
^(.(?!chocolate))*$
```
