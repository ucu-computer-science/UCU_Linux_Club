## Everything is available in AUR (using `yay`)

### Text programs for the terminal

#### AUR package manager
- [yay](https://github.com/Jguer/yay)

##### How to install Yay

in the terminal emulator

```
sudo pacman -S git
cd ~/Downloads
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```
Also, needed to add this to the end of `pacman.conf` file
```
sudo nvim /etc/pacman.conf
```
**[archlinuxfr] </br>
SigServer = Never </br>
Server = http://repo.archlinux.fr/$arch </br>**

#### For extended Shell
- [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh)

#### Terminal multiplexor
- screen (old)
- [tmux](https://github.com/tmux/tmux/wiki) (new)

#### Text editor
- [neovim](https://neovim.io/) (new)
- vi (present on every linux/unix based machine)
- nano
- [micro](https://micro-editor.github.io/)

#### File manager
- [ranger](https://github.com/ranger/ranger)
- [mc](https://midnight-commander.org/)

#### Browser
- [w3m](http://w3m.sourceforge.net/)

#### File listers
- ls (present on every linux/unix machine)
- [k](https://github.com/supercrabtree/k)
- colorls (in yay - ruby-colorls)

#### Changing directory
- cd (present on every linux/unix machine)
- [z](https://github.com/agkozak/zsh-z)

#### System monitoring
- top (by default)
- [gotop](https://github.com/cjbassi/gotop) (my favorite)
- [gtop](https://github.com/aksakalli/gtop)
- htop

#### Image viewer
- [tiv](https://github.com/stefanhaustein/TerminalImageViewer)

#### Python interpreter
Basic Python interpreter, called CPython (python3 in the terminal), is good enough, but it is not very fast and has no features
- IPython - have a beautiful interface with autocomplete
- PyPy - very fast interpreter (about 20-30 times faster)

#### For git management
- [lazygit](https://github.com/jesseduffield/lazygit)

#### For fun
- [cmatrix](https://github.com/abishekvashok/cmatrix)
- sl
- cowsay
- espeak
- hollywood
- [Color-Scripts](https://github.com/stark/Color-Scripts)
- [conky](https://github.com/brndnmtthws/conky)

### Recommended GUI programs

#### For photos view
- PhotoQT
- Gnome eye
- gThumb

#### Video player
- VLC
- Mplayer

#### Terminal emulator
- terminology
- termite
- Guake

#### Browsers
- Chromium
- Google chrome
- Firefox

#### Torrent
- QBitTorrent

#### Notepad
- leafpad
- gedit
- neovim-qt

#### Markdown editor
- Boostnote

#### Graphical yay alternative 
- pamac-aur

#### 3d modeler
- Blender

#### Photo editors
- Darktable
- GIMP

#### File manager
- nautilus (default in Gnome3)
- total commander
- double commander

#### System monitoring
- [netdata](https://github.com/netdata/netdata)
- cpu-x (IMHO, the best one)

#### Instead of Microsoft Word packet
- Google docs, sheets, impress. Available online on every PC.
- LibreOffice

#### FTP cliente
- Filezilla

#### For astronomy
- Kstars

#### For disks management
- GParted

