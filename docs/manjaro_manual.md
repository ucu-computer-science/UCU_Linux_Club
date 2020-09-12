## Manjaro Installation Guide

**You'll need an Internet connection, laptop with some spare disk space, and a USB flash drive.**

1. [Download](https://manjaro.org/download/) Manjaro `.iso` file with desktop manager of your choosing (XFCE, KDE Plasma, GNOME) 

1. Burn an `.iso` file to a USB drive:
	1. Windows
		1. Using `rufus`
			1. [Download and install rufus](https://rufus.ie/).
			2. Choose an .iso file and a USB drive, burn it and accept the 'format' dialog.
	1. Linux
		1. CLI using `dd`
			1. Check the list of your drives using `lsblk` before inserting your USB and after, remember its name.
			1. Run `sudo dd bs=4M if=<iso_file> of=<device_name> conv=fdatasync`. dd is a utility that allows to copy and move files, with `if` representing input file, and `of` - output file. `bs` represents the number of bytes to write at a time, and `conv` allows for safe finished file transfer.
		1. Using `etcher`
			1. Choose the file to burn, choose the drive and let it do its job.
	1. MacOS
		1. Have no idea. Is anyone using it anyway?

1. Free up some space (can skip this step if you have an empty drive)

1. Create a new partition with all the free space (if you want to have a dual-boot)

	1. Shrink your Windows partition with the native 'Partition' app

1. Install the operating system on the new partition

	1. Turn your laptop off and insert the USB drive, enter BIOS mode (by repeatedly tapping `esc` or `f1-f5` keys) and boot from the USB drive.

	1. Press `enter` and wait for the system to load, open the install manager, select all the settings you require.

	1. On the partitioning stage, choose `manual partitioning` and create a new GPT partition table, if needed. Afterwards, split the free space into:

		1. Create a `boot/efi` partition. File system: FAT32, Mount point: /boot/efi, Flags: boot, Size: 512mib

		1. Create a `root` partition, all your main programs are going to be located here. File system: ext4, Mount point: /, Flags: none, Size: 20-30gb

		1. Create a `swap` partition. File system: linuxswap, Flags: swap, Size: the same size as your RAM

		1. Create a `home` partition. File system: ext4, Mount point: /home, Flags: none, Size: all the rest of the space, for a minimum of 20gb

	1. Choose `next` and proceed with the installation. After it asks to restart, accept and pull the USB drive out once your laptop turns off.
	
	1. Install necessary packages for AUR usage
	
	```shell
	sudo pacman -S fakeroot binutils patch
	```
	
	1. Update the system
	```
	sudo pacman -Syu	
	```

	1. You should be all set! Proceed to [programs list](./programs.md), [resources](./resources.md) and [useful links](./useful_links.md) docs.
