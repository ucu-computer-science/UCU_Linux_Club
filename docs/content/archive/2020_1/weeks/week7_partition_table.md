+++
title = "Week 7 Homework"
date = 2021-04-05
+++
## Partition table homework

This homework won't be hard. So, what do you need to do:

### Task 1 (preparation)
- Download Arch Linux iso from official site: ([link](https://www.archlinux.org/download/))
- Setup virtual machine (Boxes, VMware, VirtualBox... - up to you)
- Create virtual machine with disk of 4 Gb (after finishing homework you can erase it)
- Launch Arch Linux iso into virtual mashine


### Task 2
All this things you should do on virtual machine, as you may damage your partition table!

You need to create a new GTP table and a number of partitions
You can use `cfdisk` or `parted` to do it.
Steps to do:
- Create empty GPT partition table
- Create 4 partitions, each 1 Gb
- Set partition types (EFI system, Linux swap, Linux home, Linux filesystem)
- Write partition table (only on virtual machine!)

As result you should write short text about which commands you used, which menu opened etc.
Save this file as `report_partitions.txt`

Also, after your work you should take a screenshot of command `fdisk -l` that will show your work and save it as `report_partitions.jpg`


### Some useful links:
[Cfdisk usage](https://www.geeksforgeeks.org/cfdisk-command-in-linux-with-examples/)

[parted documentation](https://www.gnu.org/software/parted/manual/parted.html)


