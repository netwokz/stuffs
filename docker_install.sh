#! /bin/bash

# check if not running as root
test "$UID" -gt 0 || { info "don't run this as root!"; exit; }

# ask for user password once, set timestamp. see sudo(8)
info "setting / verifying sudo timestamp"
sudo -v

sudo apt install ca-certificates curl gnupg lsb-release -y

sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor > /etc/apt/trusted.gpg.d/docker-archive-keyring.gpg
sudo echo "deb [arch=$(dpkg --print-architecture)] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

sudo apt update -y
sudo apt install docker-ce docker-ce-cli containerd.io -y

sudo curl -sL "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
