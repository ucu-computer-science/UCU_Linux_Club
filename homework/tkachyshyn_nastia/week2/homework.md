
1. Write a program that prints your ip adress.
2. List all installed programs which contain `apps` or `cs` or `ba` case insensitive separated with `->`. Example: `pr_apps.py->cs2->ba_11`. Hint: to list all installed packages use `pacman -Q`
3. Write a keylogger. As a command line argument it takes a file path where to store logs. If the log file or path do not exist, the program should create them. Each command that user entered should be prefixed with timestamp (`[year:month:day|hour:min:sec]`). The commands should work as in the usual command line. Prompt of the keylogger can be any symbol or string (e.g. `>` or `$`).

All programs must have a description and usage examples on the very top of the file as a comment or in the README.md file.

1. echo $(hostname -i) 
2. local/appstream-glib 0.7.18-1->local/archlinux-appstream-data 20200720-1.1->local/electron5 5.0.13-7->local/pamac-cli 9.5.12-1->local/pamac-common 9.5.12-1->local/pamac-gtk 9.5.12-1->local/xapp 1.8.10-1->local/gnome-getting-started-docs 3.36.2-1 (gnome)->local/gnome-user-docs 3.36.6-1 (gnome)->local/pcsclite 1.9.0-1->local/pkcs11-helper 1.26.0-2->local/baobab 3.34.1-1 (gnome)->local/bash 5.0.018-1->local/bashrc-manjaro 5.0.018-1->local/zbar 0.23.1-2


