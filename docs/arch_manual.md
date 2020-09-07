# Installing Arch

*The basis for this tutorial is [this one](https://sollus-soft.blogspot.com/2017/01/arch-linux-windows-10-uefi-systemd-boot.html)*

Firstly check if you're loaded in EFI mode: `efivar -l`

On some computers Wifi won't work without turning the module on with this  command: `rfkill unblock all`

Now let's turn on Wifi. Firstly get name of your interface: `ip link` (it usually starts with 'w', i.e: 'wlan0') 
Then activate the interface: `ip link set interface_name up`.

First method: `iwctl` 
```
iwctl
station interface_name scan
station interface_name get-network
station interface_name connetct network_name
```

Second method: `iw`

Scan for networks: `iw dev interface_name scan`.

You're probably interested in 'SSID' - name of network, and 'signal' - quality ('-100' - '0'). 

And finally connect to network: `iw dev interface_name connect "your_essid" key 0:your_key`

Check if internet works with `ping google.com` (should appear messages with '64 bytes' at the beginning, press CTRL+C to finish check)

Time synchronization: `timedatectl set-ntp true`

Now let's look at your previous boot records: `efibootmgr` and delete previous linux or some other stuff: `efibootmgr -b X -B`, where 'X' is number of stuff's boot

Now disk management: `cfdisk`. Here I delete everything from previous system and 
- choose  root directory (about 50GB, linux filesystem) 
- boot partition (1GB, EFI filesystem) (Actually it's better to install bootloader on the Windows EFI partition, if you want to see choise of system during loading). 
- Don't touch (or create if it's your first installation) home directory (40GB, linux filesystem). 
- Create swap partition (4-8GB, Linux swap)
Don't forget to "write" after making new partition. 

Now format partition and mount them. Root:
```
mkfs.ext4 /dev/sda{root number} -L "ARCH"
mount /dev/sda{root number} /mnt
```
Boot:
```
mkdir -p /mnt/boot
mkfs.fat -F32 /dev/sda{boot number}
mount /dev/sda{boot number} /mnt/boot
```
Or just mount Windows EFI partition, if you didn't create new one
```
mount /dev/sda{windows boot number} /mnt/boot
```
Swap:
```
mkswap /dev/sda{swap num}
swapon /dev/sda{swap num}
```

Now let's update pacman: `pacman  -Syy`

Install base system and packet for future AUR using: `pacstrap /mnt base linux linux-firmware base-devel linux-headers`

Generate fstab: `genfstab -U /mnt >> /mnt/etc/fstab`

Check if it is generated: `nano /mnt/etc/fstab`
You can take fstab from **configs** dir in this repo, (don't forget to change filesystem UUIDs (you can find them in 'cfdisk'))
!!**IMPORTANT**!! If you have SSD, than this is extremely important to automatically activate TRIM each time it's needed. This will save lifetime of your SSD. So please, add 'discard' option to mount points in fstab (as you can see in the **configs/fstab**)

Now let's go in arch: `arch-chroot /mnt `

It is important to download text editor at the beggining: `pacman -S vim`
Take .vim directory and .vimrc file from **configs** to install cool plugins and color scheme

Adjust locals: `nano /etc/locale.gen` and uncomment
```
en_US.UTF-8 UTF-8
ru_RU.UTF-8 UTF-8
uk_UA.UTF-8 UTF-8
```
Don't forget to save

Adjust time zone and time : 
```
ln -sf /usr/share/zoneinfo/Europe/Kiev /etc/localtime
hwclock --systohc
```

Adjust name of computer: `nano /etc/hostname` and write there _"userhost - YOUR_USERNAME"_

Adjust hosts: `nano /ets/hosts` and write there -_"127.0.0.1 pavlik_giley.localdomain YOUR_USERNAME"-_ 
DONT FORGET TO SAVE EVERYTHING

Password for root: `passwd` 

Add new user: `useradd -G wheel -s /bin/bash -m YOUR_USERNAME`, and give him sudo permissions: `nvim /etc/sudoers` 
and uncomment _"%wheel ALL=(ALL) ALL"_

user's password: `passwd YOUR_USERNAME`

Download some potentially useful stuff: `pacman -S  efibootmgr iw wpa_supplicant dialog netctl dhcpcd`.
And more: `pacman -S ntfs-3g mtools fuse2`

Install bootloader: `bootctl install`

Loader config: `vim /boot/loder/loader.conf` and copy
**configs/loader.conf**

Now it is vital to adjust kernel settings: 
```
pacman -S intel-ucode
vim /boot/loader/entries/arch.conf
```
Write here :
copy from **configs/arch.conf**

Now exit and umount all partition:
```
exit
umount -R /mnt
reboot
```

# GNOME installation

Install X: `sudo pacman -S xorg-server xorg-xinit xorg-apps mesa-libgl xterm`

Install graphic drivers:
```
sudo pacman -S xf86-video-intel
sudo pacman -S nvidia
```

Now install GNOME itself:
```
sudo pacman -Syu
sudo pacman -S gnome
systemctl enable NetworkManager
systemctl enable gdm
```

Lenovo y530 can't render HDMI output with intel GPU, so if you want to use second monitor, take **configs/xorg.conf** and replace it in /etc/X11/
It will render the whole gnome session with nvidia. If you want to save battery life, then replace `Screen 0 "nvidia"` with `Screen 0 "intel"` and reboot
Also download prime-run: `sudo pacman -S prime-run`
More details [here](https://wiki.archlinux.org/index.php/PRIME#PRIME_render_offload)

# System customization and apps installation
First of all set normal wallpalers, change touchpad sensitivity and other settings in GNOME

Python: 
```
sudo pacman python-pip
sudo pacman ipython
```

Battery optimization:
```
sudo pacman -S tlp
sudo tlp start
sudo systemctl enable tlp.service
```

It's a good idea to create new mirrorlist file for Pacman, if you from Ukraine, you can use mine (**configs/mirrorlist**). replace it in /etc/pacman.d/

Terminal: `sudo pacman -S terminator`

git: `sudo pacman -S git`

yay: `git clone https://aur.archlinux.org/yay.git; cd yay; makepkg -si`

zsh instllation and customization with oh my zsh:
```
cd ~
sudo pacman -S zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
```
Then copy **configs/.zshrc** to home directory

Browser + telegram: 
```
yay telegram-desktop
yay firefox
```
Don't forget to sign in gmail, youtube, CMS, etc.

CUSTOMIZATION
```
sps gnome-tweaks
```
Download all extension and setup tweask as you see on screenshots from **screenshots** dir
Also you can find themes, fonts and icons in **configs** dir (.themes, .icons, .fonts)

Install VScode: `yay visual-studio-code-insiders`

Cion `yay clion #chose just clion`. Don't forget to activate licension and type path to compilers and debugger

Pycharm `yay pycharm #choose community version` Don't forget to install material theme and set 18's font

STM32. Install eveything except eclipse from [this tutorial](https://gist.github.com/Myralllka/42385fdecacb7cc2a45ec9376b57a4b2)
After this download STM32CubeMX itself from [official site](https://www.st.com/en/development-tools/stm32cubemx.html)
Then unzip script, give permissions to run it (chmod +x scriptname.sh) and run it with sudo

Then if you will have problems with debuggger run those commands:
```
cd /usr/lib
sudo ln -s libncursesw.so.6.1 libncurses.so.5
sudo ln -s libncursesw.so.6.1 libtinfo.so.5
```
Follow [this tutorial](https://cms.ucu.edu.ua/pluginfile.php/181558/mod_resource/content/1/CLion_STM32_Settings.pdf) to work with STM32 through CLion: 

List of other apps I use:
1. Slack
2. IntellijIDEA (don't forget to get jdk)
3. AndroidStudio (+sdk +ndk)
4. zoom
5. Microsoft Teams ('teams' package in local repository)
6. clion-gui
7. LibreOffice

Also it's quite useful to configurate your touchpad gestures with [this](https://github.com/bulletmark/libinput-gestures) application
Looks like that's it. Happy archlinux experience!

