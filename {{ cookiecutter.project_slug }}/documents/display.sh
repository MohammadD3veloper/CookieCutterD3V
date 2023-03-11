#!/bin/bash

# Displaying markdown documents
function displayDocuments() {
    echo -e "[+] Displaying About.md ..."
    glow About.md
    echo -e "[+] Displaying Development.md ..."
    glow Development.md
    echo -e "[+] Displaying Production.md ..."
    glow Production.md
}

# Checking user permission
function checkUser() {
    if ! [ $EUID == 0 ]; then
        echo -e "[-] Sorry, This script should be run in sudo :(."
        exit
    fi
}

checkUser

# Check distru for glow installation
if ! [ "$(command -v glow)" ]; then
    if [ -d /etc/apt/ ]; then
        apt update 1> /dev/null | echo -e "[*] Updating repositories"
        apt install glow -y 1> /dev/null | echo -e "[*] Installing glow..."
    elif [ -f /etc/pacman.conf ]; then
        pacman -Sy 1> /dev/null | echo -e "[*] Updating repositories"
        pacman -S glow --noconfirm 1> /dev/null | echo -e "[*] Installing glow..."
    elif [ -f /etc/yum.conf ]; then
        yum update 1> /dev/null | echo -e "[*] Updating repositories"
        yum install glow -y 1> /dev/null | echo -e "[*] Installing glow..."
    fi
fi

# Run glow to show markdown files
displayDocuments