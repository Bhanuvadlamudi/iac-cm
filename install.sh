#!/bin/bash

sudo apt-get update
echo "@@@@@@@@@@@@@@@@@@@@   Updated   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

#python
echo "@@@@@@@@@@@@@@@@@@@@   Installing python3   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
sudo apt-get install python3
echo "@@@@@@@@@@@@@@@@@@@@   Python3 version  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
python3 --version

# setup pip
echo "@@@@@@@@@@@@@@@@@@@@   Installing pip3   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
sudo apt install python3-pip
echo "@@@@@@@@@@@@@@@@@@@@   pip3 version   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
pip3 --version

#ansible
echo "@@@@@@@@@@@@@@@@@@@@   Installing ansible   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
sudo apt-get install ansible --upgrade
echo "@@@@@@@@@@@@@@@@@@@@   Ansible version   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
ansible  --version

#terraform
echo "@@@@@@@@@@@@@@@@@@@@   Installing terraform   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
sudo apt-get install unzip
wget https://releases.hashicorp.com/terraform/0.11.11/terraform_0.11.11_linux_amd64.zip
unzip terraform_0.11.11_linux_amd64.zip
sudo mv terraform /usr/local/bin/
echo "@@@@@@@@@@@@@@@@@@@@   Terraform version   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
terraform --version

echo "############################ SUCESSFULLY INSTALLED ######################"
