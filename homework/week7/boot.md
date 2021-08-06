# Bootloader homework
This week you had a lecture about booting and bootloaders in particular. Even though they are very small they still can cause a lot of troubles. In this homework, you don't need to submit anything, though it doesn't mean that you should do nothing. You have a few tasks below with the most common problems and just useful things.
#####
If you are a happy owner of mac than these tasks aren't for you. But you still have your own homework: as we didn't talk about mac bootloader, please find out more about it.
### Hello, BIOS!
I have heard that some of you still don't know how to access BIOS setup. So your first task will be to boot from it :)
###
BIOS setup is also very small, but have many useful and interesting settings. I do not recommend you to play with them unless you want to crash your computer, but highly recommend you to read more about them.
###
As Linux user, you often will need to boot from USB (flash drive) and you can do this from BIOS, so, this task is MANDATORY! If you won't know how to boot from USB after this homework - shame on you ^^.
([For lazy ones](https://www.tomshardware.com/reviews/bios-keys-to-access-your-firmware,5732.html)) Hope you will be able to find out how to boot Linux/Windows from it.
### More space
As I have noted boot loaders are really small, so most companies initially put 100 MB on them. But now your bootloader has to deal with two OS (or even more), so they need more space. Firstly, check how much space it already has:
```
lsblk
```
This will show you all your partitions, you just need to find one with '/boot' mark.([more commands for partitions](https://www.cyberciti.biz/faq/linux-check-boot-path-command/)).
![image](https://user-images.githubusercontent.com/54356826/100021860-0ed6a300-2dda-11eb-8e27-be899b3857cc.png)
###
As you can see I allocated 900MB for my boot 0_0 I think for you 500MB will be more than enough. If you already have 200MB+ than it isn't so critical for you...maybe... But if you have only 100MB it is mandatory for you to increase it to 500!
###
I know that you are new to Linux, so was I when I faced with a boot memory problem. So you have no excuses for not doing this part!
### Try something new
(Plz, do not hate me for this task)
###
I know that most of you didn't install Linux by themselves(someone did it for you). So you probably don't know how to install and set bootloader. Change your bootloader (systemd-boot <-> GRUB), delete previous one (for users that have already changed something in their boot loaders' config: don't delete files with configs), do some tasks for it and go back to your previous bootloader, or stay on a new one if you like it more. (Some guides below)
####
(If you have another bootloader than it probably will be better if you change it to systemd-boot|GRUB)
#### Systemd-boot (only for UEFI users)
Check whether you have UEFI or BIOS.
####
I hate when I have only 5, 4, 3, 2, 1.... \*\*\*\*! seconds to choose the wanted OS. Haven't you changed it yet? If no, then it is a perfect time for it! Make your bootloader more comfortable.
###
Systemd-boot doesn't give you so many configurations as GRUB. But still, try to find out how to autoload another OS (a task with *) Useful site
[Useful site](https://wiki.archlinux.org/index.php/Systemd-boot#Loader_configuration)
###
Switch to GRUB now (install grub, mount it, remove systemd-boot (REMEMBER THAT SOME COMMANDS YOU CAN EXECUTE ONLY FROM ROOT (sudo su)).
#### GRUB
The same task to change your timer :) Remember what GRUB files you can edit and what you don't need to touch?
####
Find where GRUB add your Arch|Manjaro and Windows(another second OS) to the menu (do not change anything). It may help you if GRUB doesn't add all OS automatically and you need to do it by yourself. Big hint:
```
cd /etc/grub.d
```
Change your theme (task with *, for ones that will stay with GRUB).
###
If you are familiar with GRUB and want to do something harder then try to put a password on it :)
###
[Hints](https://ostechnix.com/configure-grub-2-boot-loader-settings-ubuntu-16-04/) BUT DO NOT USE Grub-customizer!!!
###
Change GRUB to systemd-boot (scroll to the bottom and do exactly like this [guy](https://bbs.archlinux.org/viewtopic.php?id=223909))
### Some links to refresh information from lecture:
+ [Cool guy](https://www.youtube.com/watch?v=zIYkol851dU&ab_channel=Techquickie)
+ [Boot issues (actually more for next week)](https://www.tecmint.com/find-and-fix-linux-boot-issues/)
+ [GRUB issues](https://www.unixmen.com/fixing-a-few-common-grub-errors-broken-bootloader-and-error-1715/)
+ [Systemd-boot](https://fedoraproject.org/wiki/How_to_debug_Systemd_problems)
+ [BIOS|UEFI](https://askubuntu.com/questions/173248/where-is-the-bootloader-stored-in-rom-ram-or-elsewhere)
+ [Multiboot USB](https://www.linuxbabe.com/apps/create-multiboot-usb-linux-windows-iso#:~:text=To%20create%20a%20multiboot%20usb%2C%20first%20insert%20your%20USB%20flash,specify%20the%20persistent%20file%20size.)
