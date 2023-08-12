#!/bin/bash

# Check for arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: ./git_install.sh Your_Name email@example.com"
    exit 1
fi

NAME=$1
EMAIL=$2

sudo pacman -S git
git config --global user.name "$NAME"
git config --global user.email "$EMAIL"
