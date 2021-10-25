#!/bin/bash

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

ln -fs $SCRIPT_DIR/git/.gitconfig ~/.gitconfig
ln -fs $SCRIPT_DIR/bash/.bashrc ~/.bashrc
#ln -fs $SCRIPT_DIR/git/.gitconfig ~/.gitconfig
