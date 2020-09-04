## Manjaro Installation Guide

**You'll need an Internet connection, laptop with some spare disk space, and a USB flash drive.**

1. [Download](https://manjaro.org/download/) Manjaro `.iso` file with desktop manager of your choosing (XFCE, KDE Plasma, GNOME) 

1. Burn an ``.iso` file to a USB drive:
	1. Windows
		1. Using ``rufus`
			1. [Download and install rufus](https://rufus.ie/).
			2. Choose an .iso file and a USB drive, burn it and accept the 'format' dialog.
	1. Linux
		1. CLI using `dd`
			1. Check the list of your drives using `lsblk` before inserting your USB and after, remember its name.
			1. Run `sudo dd bs=4M if=<iso_file> of=<device_name> conv=fdatasync`. dd is a utility that allows to copy and move files, with `if` representing input file, and `of` - output file. `bs` represents the number of bytes to write at a time, and `conv` allows for safe finished file transfer.
		1. Using ``etcher`
			1. Choose the file to burn, choose the drive and let it do its job.
	1. MacOS
		1. Have no idea. Is anyone using it anyway?

1. Free up some space (can skip this step if you have an empty drive)

	1. TODO: Add all the details with screenshots

1. Install the operating system

	1. TODO: Add all the details with screenshots

