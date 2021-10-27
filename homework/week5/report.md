## Week 5 RegEx Homework

### You should use this doc as a template, fork the repository, fill in the answers, push changes to your repo, create pull request and add Lesi-N as a reviewer.
### Your task is to go to [this website](http://regextutorials.com/excercise.html) and complete all 21 challenges

### Try and complete them  without consulting external sources; if you get stuc on one,  move on and come back to it later. If you're still having difficulties, use the hints and try to understand them. Good luck!

---

Paste your answers below the corresponding numbers

1.
\d+\.\d+
2.
(.*\(19[0-8]\d\)|.*\(189\d\))
3.
#[0-9A-F]{6}
4.
#([\dA-Fa-f]+)\1\1
5.
.{30}.+
6.
(\s[\w'-]+)\1 -> $1
7.
<.+?>
8.
(\d+\.\d\d)\d+ -> $1
9.
(\d)(?=(\d\d\d)+\b) -> $1,
10.
function [a-z].+?\)
11.
(\d\d\d\d)-(\d\d)-(\d\d) -> $3.$2.$1
12.
((0|1)\d|2[0-3]):[0-5]\d
13.
\b(0?\d|11):[0-5]\d(\s+AM|\s+PM)
14.
;(?=.+\)) -> ,
15.
var\s+(.+?)\s+=\s+new\s+(.+?)(?=\() -> $2 $1
16.
([\da-f]{0,4}:){2,}[\da-f]{0,4}
17.
#([\da-f]{2}){3,4}\b
18.
(\b[\w\d\(\).*]+?)\s+\+\s+([\w\d\(\).*]+) -> Add($1, $2)
19.
\?.+\b
20.
http://.+?(?=(\?|/))
21.
^(?!.+?chocolate).+$



