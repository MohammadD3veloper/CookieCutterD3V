#!/bin/bash

# Check distru for glow installation
if ! [ $(command -v glow) == 0 ] then
    if [ -d /etc/apt/ ] then
        apt install glow -y
    elif [ -f /etc/pacman.conf ] then
        pacman -S glow --confirm
    elif [ -f /etc/yum.conf ] then
        yum install glow -y
    fi

# Run glow to show markdown files
else
    glow About.md
    glow Development.md
    glow Production.md
fi
