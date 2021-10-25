#!/bin/bash

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd $SCRIPT_DIR && git pull

ln -fs $SCRIPT_DIR/git/.gitconfig ~/.gitconfig
ln -fs $SCRIPT_DIR/bash/.bashrc ~/.bashrc

ln -fs $SCRIPT_DIR/neofetch/ ~/.config/
#ln -fs $SCRIPT_DIR/git/.gitconfig ~/.gitconfig
