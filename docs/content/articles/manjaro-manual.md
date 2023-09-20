+++
title = "Manjaro installation manual"
date = 2019-11-27
[taxonomies]
tags = ["Manjaro Linux", "Installation", "Manual"]
+++

## Manjaro Installation Guide

**You'll need an Internet connection, laptop with some spare disk space, and a USB flash drive.**

1. [Download](https://manjaro.org/download/) Manjaro `.iso` file with desktop manager of your choosing (XFCE, KDE Plasma, GNOME)
2. Burn an `.iso` file to a USB drive:

   1. Windows
      1. Using `rufus`
         1. [Download and install rufus](https://rufus.ie/).
         2. Choose an .iso file and a USB drive, burn it and accept the 'format' dialog.
   2. Linux
      1. CLI using `dd`
         1. Check the list of your drives using `lsblk` before inserting your USB and after, remember its name.
         2. Run `sudo dd bs=4M if=<iso_file> of=<device_name> conv=fdatasync status="progress"`. dd is a utility that allows to copy and move files, with `if` representing input file, and `of` - output file. `bs` represents the number of bytes to write at a time, and `conv` allows for safe finished file transfer.
      2. Using `etcher`
         1. Choose the file to burn, choose the drive and let it do its job.
   3. MacOS
      1. Have no idea. Is anyone using it anyway?
3. Free up some space (can skip this step if you have an empty drive)
4. Create a new partition with all the free space (if you want to have a dual-boot)

   1. Shrink your Windows partition with the native 'Partition' app
5. Install the operating system on the new partition

   1. Turn your laptop off and insert the USB drive, enter BIOS mode (by repeatedly tapping `esc` or `f1-f5` keys) and boot from the USB drive.
   2. Press `enter` and wait for the system to load, open the install manager, select all the settings you require.
   3. On the partitioning stage, choose `manual partitioning` and create a new GPT partition table, if needed. Afterwards, split the free space into:

      1. Create a `boot/efi` partition. File system: FAT32, Mount point: /boot/efi, Flags: boot, Size: 512mib
      2. Create a `root` partition, all your main programs are going to be located here. File system: ext4, Mount point: /, Flags: none, Size: 20-30gb
      3. Create a `swap` partition. File system: linuxswap, Flags: swap, Size: the same size as your RAM
      4. Create a `home` partition. File system: ext4, Mount point: /home, Flags: none, Size: all the rest of the space, for a minimum of 20gb
   4. Choose `next` and proceed with the installation. After it asks to restart, accept and pull the USB drive out once your laptop turns off.
   5. Install necessary packages for AUR usage

   ```shell
   sudo pacman -Syy
   sudo pacman -S fakeroot binutils patch
   ```
   1. Update the system (we recommend you do that at least once a week)

   ```shell
   sudo pacman -Syu
   ```
   1. You should be all set! Proceed to [programs list](@/articles/programs.md), [resources](@/articles/resources.md) and [useful links](@/articles/useful-links.md) docs.
