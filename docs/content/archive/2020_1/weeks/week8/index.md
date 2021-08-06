+++
title = "Week 8 Homework"
date = 2021-04-05
+++
# Week 8: systemd, systemctl, rfkill, kernel options, etc.

### [**Presentation**](https://docs.google.com/presentation/d/e/2PACX-1vSwRYb0LULiq0EGpJ1adne2e4W9_QAgsNcM1R825YCBey9WprUD_rWw9lmQuCYcVD7RZJcQRxVujCRJ/pub?start=false&loop=false&delayms=3000)

### Homework
1) Create unit that will get all messages from the last boot with errors/warning/debug to some log file. There should be a config file, where u state, which priority messages to save.

*Hint: Use journalctl and dmesg*

2) Rewrite hello_world unit from the lecture using the timer (If systemd refuses to start a unit each second, trigger it each 10 sec)

3) write a timer unit that clears all versions except for the last version of the package in pacman cache.

*Hint: paccache*

All details, like syntax for the config in 1) are up to you. (But bash for scripting is prefered)  Just write good README with explanations. If you want to add some functionality, go ahead!

Useful links for the homework:

- [ArchWiki on timers](https://wiki.archlinux.org/index.php/Systemd/Timers)
- First two links from useful links below

### Useful links to read
- [A beautiful article about units](https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files)
- [systemd documentation](https://www.freedesktop.org/software/systemd/man/)
- [systemd documentation about services](https://www.freedesktop.org/software/systemd/man/systemd.service.html#)
- [russian archwiki systemctl](https://wiki.archlinux.org/index.php/Systemd_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)#%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B_%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_systemctl)
- [joutnalctl facilities (and just journalctl on archwiki)](https://wiki.archlinux.org/index.php/Systemd/Journal#Facility)
- [kernel parameters archwiki](https://wiki.archlinux.org/index.php/kernel_parameters)
- [systemd boot archwiki](https://wiki.archlinux.org/index.php/systemd-boot)
- [тут можна знайти кілька хороших відосів де стрьомний мужик розказує і про sytemd і про юніти і взагалі про лінукс](https://www.youtube.com/playlist?list=PLWCdmr_xDegfmNxUhbLAC4YxIvlnzY9U9)

### Questions?
My telegram: @pavlohiley

think twice before writing -_-
