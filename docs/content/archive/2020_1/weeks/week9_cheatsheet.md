+++
title = "Week 9 Cheatsheet"
date = 2021-04-05
+++
## Compilation

After setting up your IDE (VS Code, JetBrains CLion, Vim are among many 
of the options available) and having your program ready, you have to compile it
(i.e. turn the text of the program into a machine code which your computer will
be able to run later).

This can be done like this, in your terminal:
```
gcc programname.c -o outputname
```

If there were errors or notes during the compilation process, the compiler 
(here we are using the GCC compiler) will notify you. If the program compiled 
correctly, you can later run the generated executable:
```
./outputname
```

## General tutorial

### Code

Code for execution goes into files with “.c” suffix.  Shared decl’s 
(included using #include “mylib.h”) in “header” files, end in “.h”

### Comments

Characters to the right of `//` are not interpreted; they’re a comment. 
Text between `/*` and `*/` (possibly across lines) is commented out as well. 

### Data types 

* `char` - an ASCII value: e.g. ‘a’ (see: man ascii)
* `int` - a signed integer: e.g. 97 or hex 0x61, oct 0x141  
* `float` - a floating-point (possibly fractional) value  
* `double` - a double length float 

`char`, `int`, and `double` are most frequently and easily used in small 
programs.

sizeof(double) computes the size of a double in bytes.

Zero values represent logical false, nonzero values are logical true.

### Functions

A function is a pointer to some code, parameterized by formal parameters, 
that may be executed by providing actual parameters. Functions must be 
declared before they are used, but code may be provided later. 

A `sqrt` function for positive `n` might be declared as:  

```
int addNumbers(int a, int b)         // function definition with return type, name and parameters
{
    int result;
    result = a+b;
    return result;                  // return statement
}
Functions that do not return anything return `void`.
There must always be a main function that returns an int:
```
```c
int main() 
{
	return 0;
}
```

### Statements

Angle brackets identify syntactic elements and don’t appear in real 
statements

```c
<expression> ; //semicolon indicates end of a simple statement  
break; //quits the tightest loop or switch immediately  
continue; //jumps to next loop test, skipping rest of loop body  
return x; //quits this function, returns x as value  
if (<condition>) <stmt>! //stmt executed if cond true (nonzero)  
if (<condition>) <stmt> else <stmt> // two-way condition  
while (<condition>) <stmt>    //repeatedly execute stmt only if condition true  
do <stmt> while (<condition>); //note the semicolon, executes at least once
for (<init>; <condition>; <step>) { <statements> }
```

### Includes

The homework requires you to include several header files with the needed functions:

#### I/O (`#include <stdio.h>`)
Default input comes from “stdin”; output goes to “stdout”; errors to “stderr”.
Standard input and output routines are declared in `stdio.h`: `#include <stdio.h>`
* `scanf(p,...)` - reads ... args using format p (below); 
* `printf(p, ...)` - write ... args using format p (below); pass args as is  fprintf(f,p,...)  

Format specifiers:
`%c` - character
`%d` - decimal integer 
`%s` - string
`%f` - float

#### MEMORY (`#include <stdlib.h>`)
* `malloc(n)` - allocates `n` bytes of memory; (for type T: `p = (T*)malloc`)
