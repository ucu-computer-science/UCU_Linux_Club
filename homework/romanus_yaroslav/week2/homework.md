1. Write a program that prints your ip adress.
2. List all installed programs which contain `apps` or `cs` or `ba` case insensitive separated with `->`. Example: `pr_apps.py->cs2->ba_11`. Hint: to list all installed packages use `pacman -Q`
3. Write a keylogger. As a command line argument it takes a file path where to store logs. If the log file or path do not exist, the program should create them. Each command that user entered should be prefixed with timestamp (`[year:month:day|hour:min:sec]`). The commands should work as in the usual command line. Prompt of the keylogger can be any symbol or string (e.g. `>` or `$`).

All programs must have a description and usage examples on the very top of the file as a comment or in the README.md file.


'Я не знаю як ок написати опис та приклади тому най буде як є'


task1

Return the ip of user

Example:
./task1
1010.2.34.567

The main part:
#!/bin/bash
ip a | tail -4 | head -1 > ip
cut -b 10- ip | cut -d/ -f'1'


task2

Return the list of all programs with 'apps','cs' or 'ba' in it in appropriate view

Example:
./task2
pr_apps.py->cs2->ba_11

The main part:
#!/bin/bash
pacman -Q | grep -e cs -e apps -e ba > file
paste -s -d : file > file1
sed 's/:/->/g' file1 > file
cat file


task3 was too hard-_-
