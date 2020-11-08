# week 8: systemd, systemctl, rfkill, kernel options, etc.

### [**presetation**](https://docs.google.com/presentation/d/e/2PACX-1vSwRYb0LULiq0EGpJ1adne2e4W9_QAgsNcM1R825YCBey9WprUD_rWw9lmQuCYcVD7RZJcQRxVujCRJ/pub?start=false&loop=false&delayms=3000)

### homework
1) create unit that is getting all messages from last boot with errors/warning/debug/ to some log file. There should be config file, where u state, what priority messages to save.

Hint: Use journalctl and dmesg
2) rewrite hello_world unit from lecture using timer (If systemd refuses to start unit each second, trigger it each 10 sec)
3) write timer unit that clears all exept last version of package in pacman cache

Hint: paccache

All details, like syntax for config in 1) or needed parameters in units are up to you. (But bash for scripting is prefered)  Just write good README. If you want to extend some task, add some functionality, that's nice.

Useful links for hw:
[archwiki on timers](https://wiki.archlinux.org/index.php/Systemd/Timers)
first two links from useful links bellow |
					 v

### useful links to read
- [beautiful article about units](https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files)
- [systemd documentation](https://www.freedesktop.org/software/systemd/man/)
- [systemd documentation about services](https://www.freedesktop.org/software/systemd/man/systemd.service.html#)
- [russian archwiki systemctl](https://wiki.archlinux.org/index.php/Systemd_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)#%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B_%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_systemctl)
- [joutnalctl facilities (and just journalctl on archwiki)](https://wiki.archlinux.org/index.php/Systemd/Journal#Facility)
- [kernel parameters archwiki](https://wiki.archlinux.org/index.php/kernel_parameters)
- [systemd boot archwiki](https://wiki.archlinux.org/index.php/systemd-boot)
- [тут можна знайти кілька хороших відосів де стрьомний мужик розказує і про sytemd і про юніти і взагалі про лінуксс](https://www.youtube.com/playlist?list=PLWCdmr_xDegfmNxUhbLAC4YxIvlnzY9U9)

### Questions?
My telegram: @pavlohiley
think twice before writing -_-
