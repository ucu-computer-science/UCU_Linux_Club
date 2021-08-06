+++
title = "Week 9 Homework"
date = 2021-04-05
+++

There is a short introduction and cheat sheat [available here](./week9-cheatsheet), which explains 
the basics of the C programming language and its compilation process on Linux.


## Problem 1 (Mario)

Let's recreate the pyramids from Super Mario in text:
```c
     #
    ##
   ###
  ####
 #####
######
```

So, the program should prompt the user to input the height of the pyramid
and then output the pyramid of the specified height:
```c
$ ./mario
Height: 6
     #
    ##
   ###
  ####
 #####
######
```

Other examples:
```c
$ ./mario
Height: 2
 #
##
```
```c
$ ./mario
Height: 1
#
```

## Problem 2

Create a program that takes two integer numbers as an input from the user 
(a ≤ b) and for every number in the interval [a; b] outputs: 

* the number in plain text english if it's less than 10
* otherwise, whether it's `odd` or `even`

```c
$ ./interval
Input a: 8
Input b: 11

eight
nine
even 
odd
```

Other examples:
```c
$ ./interval
Input a: 13
Input b: 15

odd
even
odd
```
```c
$ ./interval
Input a: 1
Input b: 4

one
two
three
four
```

## Problem 3

Develop a program which is going to output English text according to these rules:
* First, all the whitespace are deleted
* Let the length of the text taken as an input be `L`. 
Then, output the text as a table with the number of rows and columns, where 
`[√L] ≤ rows ≤ columns ≤ [√L] + 1` ([x] is an integer part of the number) 

For example, the message `capital is an abstract parasite, an insatiable 
vampire and zombie maker; but the living flesh it converts into dead labor 
is ours, and the zombies it makes are us` has a length of 134 symbols without 
the whitespace, we can output it in a table 12 x 12.

```c
capitalisan
abstractpar
asite,anins
atiablevamp
ireandzombi
emaker;butt
helivingfle
shitconvert
sintodeadla
borisours,a
ndthezombie
sitmakesare
us
```

You have to check whether `rows × columns ≥ L` and if there are several
possible rectangles choose the one with the smaller area.

Other examples:
```c
$ ./table
Input your text: it is time that lived moments replace the dead memory that has stamped acquaintance with the hidden restriction that nothing can ever be experienced.

Characters total: 126
Rows: 11
Columns: 12

itistimethat
livedmoments
replacethede
admemorythat
hasstampedac
quaintancewi
ththehiddenr
estrictionth
atnothingcan
everbeexperi
enced.
```

## Problem 4

Develop a program which, taking two integer arrays as its input will
create a new integer array. The new array consists of the digits of the sum of the original
two arrays' elements.

So, for the example if given two arrays {23, 5, 2, 7, 87} and {4, 67, 2, 8}, 
the new array will look like this {2, 7, 7, 2, 4, 1, 5, 8, 7}.

If the array is empty, just consider the respective elements as zeros.
Then, if given two arrays { } and {4, 67, 3, 8} then the new array will look 
like {4, 6, 7, 3, 8}.

An example usage:
```
$ ./arrays
Input the length of the first array: 5
Input the numbers: 5
23
5
2
7
87

Input the length of the second array: 5
Input the numbers: 4
4
67
2
8

The output array: 
2 7 7 2 4 1 5 8 7
```
