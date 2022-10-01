#!/bin/bash

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

#cd $SCRIPT_DIR && git pull

# git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

ln -fs $SCRIPT_DIR/gitconfig/.gitconfig ~/.gitconfig
ln -fs $SCRIPT_DIR/zsh/.zshrc ~/.zshrc
ln -fs $SCRIPT_DIR/zsh/.oh-my-zsh/ ~/
ln -fs $SCRIPT_DIR/i3/ ~/.config/
ln -fs $SCRIPT_DIR/kitty/ ~/.config/

