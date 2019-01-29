#!/bin/bash


sudo apt-get update

echo "@@@@@@@@@@@@@@@@@@@@   Updated   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"


echo "@@@@@@@@@@@@@@@@@@@@   Intsalling python3   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
#python
sudo apt-get install python3

echo "@@@@@@@@@@@@@@@@@@@@   Python3 version  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

python3 --version

echo "@@@@@@@@@@@@@@@@@@@@   Installing pip3   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

# setup pip 

sudo apt install python3-pip

echo "@@@@@@@@@@@@@@@@@@@@   pip3 version   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
pip3 --version

echo "@@@@@@@@@@@@@@@@@@@@   Installing ansible   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
#ansible

sudo apt-get install ansible --upgrade


echo "@@@@@@@@@@@@@@@@@@@@   Ansible version   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

ansible  --version 

echo "@@@@@@@@@@@@@@@@@@@@   Installing terraform   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

#terraform
sudo apt-get install unzip
wget https://releases.hashicorp.com/terraform/0.11.7/terraform_0.11.7_linux_amd64.zip
unzip terraform_0.11.10_linux_amd64.zip
sudo mv terraform /usr/local/bin/

echo "@@@@@@@@@@@@@@@@@@@@   Terraform version   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" 

terraform --version 

echo "############################ SUCESSFULLY INSTALLED ######################"






