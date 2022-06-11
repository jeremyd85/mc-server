#!/bin/bash

apt update && sudo apt upgrade -y
add-apt-repository ppa:deadsnakes/ppa -y
apt install python3.10 apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" -y
apt update
apt install docker-ce
systemctl status docker
