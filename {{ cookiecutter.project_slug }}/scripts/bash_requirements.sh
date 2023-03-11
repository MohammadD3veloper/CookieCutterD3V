#!/bin/bash


function checkRoot {
    if ! [ $EUID == 0 ]; then
        echo -e "I'm Sorry, You should run this script as root :("
        exit
    fi
}


function pkg_update {
    if [ -f /etc/apt/apt.conf ]; then
        apt update 2>&1 | echo -e "Updating repositories"
    elif [ -f /etc/pacman.conf ]; then
        pacman -Sy 2>&1 | echo -e "Updating repositories"
    elif [ -f /etc/yum.conf ]; then
        yum update 2>&1 | echo -e "Updating repositories"
    fi
}


function pkg_install {
    if [ -f /etc/apt/apt.conf ]; then
        apt install $1 $2 $3 -y 2>&1 /dev/null | echo "[*] Installing required tools..."
    elif [ -f /etc/pacman.conf ]; then
        pacman -S $1 $2 $3 --noconfirm 2>&1 /dev/null | echo "[*] Installing required tools..."
    elif [ -f /etc/yum.conf ]; then
        yum install $1 $2 $3 -y 2>&1 /dev/null | echo "[*] Installing required tools..."
    fi
}


function readyup_virtualenv {
    if ! [ -d "../.{{ cookiecutter.project_slug }}" ]; then
        cd .. && virtualenv .{{ cookiecutter.project_slug }} | echo -e "[+] Creating virtualenv on parent directory with name: .{{ cookiecutter.project_slug }}"
    else 
        echo -e "[+] Virtualenv .{{ cookiecutter.project_slug }} is already exists in parent directory."
    fi
}


function main {
    checkRoot
    echo -e "[*] Welcome to installation :D"
    pkg_update
    pkg_install docker docker-compose python-virtualenv
    readyup_virtualenv
    source ../.{{ cookiecutter.project_slug }}/bin/activate
    echo -e "[!] if venv not activated yet, use: 'source ../.{{ cookiecutter.project_slug }}/bin/activate'"
    echo -e "[+] Everything is done :)"
}

main
