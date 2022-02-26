#!/bin/bash

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd $SCRIPT_DIR && git pull

# git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

ln -fs $SCRIPT_DIR/git/.gitconfig ~/.gitconfig
ln -fs $SCRIPT_DIR/zsh/.zshrc ~/.zshrc
ln -fs $SCRIPT_DIR/suckless/ ~/.config/
ln -fs $SCRIPT_DIR/kitty/ ~/.config/
ln -fs $SCRIPT_DIR/rofi/ ~/.config/
#ln -fs $SCRIPT_dir/conky/.conkyrc ~/.config/conky/conky.conf
# ln -fs $SCRIPT_DIR/bash/.bashrc ~/.bashrc
#ln -fs $SCRIPT_DIR/themes/ ~/.themes
ln -fs $SCRIPT_DIR/nvim/ ~/.config/
#ln -fs $SCRIPT_DIR/neofetch/ ~/.config/
#ln -fs $SCRIPT_DIR/BetterDiscord/ ~/.config/

#ln -fs $SCRIPT_DIR/git/.gitconfig ~/.gitconfig
