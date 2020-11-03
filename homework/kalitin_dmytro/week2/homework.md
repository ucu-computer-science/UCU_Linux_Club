1. Write a program that prints your ip adress.
1. List all installed programs which contain `apps` or `cs` or `ba` case insensitive separated with `->`. Example: `pr_apps.py->cs2->ba_11`. Hint: to list all installed packages use `pacman -Q`
1. Write a keylogger. As a command line argument it takes a file path where to store logs. If the log file or path do not exist, the program should create them. Each command that user entered should be prefixed with timestamp (`[year:month:day|hour:min:sec]`). The commands should work as in the usual command line. Prompt of the keylogger can be any symbol or string (e.g. `>` or `$`).

All programs must have a description and usage examples on the very top of the file as a comment or in the README.md file.

2. pacman -Q | grep -E 'apps|cs|ba' | tr '\n' '\t' | sed 's/\t/->/g'