# AuToNoMoUS

A tool to automate the steps of provisioning of Infrastructure and Configuration Management to AWS for Flask web applications. This helps to deploy your applications with minimum knowledge of the tools for Iac and CM.



## Data PipeLine

![gif](https://user-images.githubusercontent.com/20710319/52317884-f04ab200-298f-11e9-9b4e-d7ff4107b319.gif)


## Getting Started

What you will need:

 1.AWS Account
 2.AWS Access, Secret keys. "Dont forget to download csv of your IAM". 
 3.Add Permissions to IAM user.


  ![screenshot from 2019-02-05 21-03-58](https://user-images.githubusercontent.com/20710319/52316614-37ce3f80-298a-11e9-9884-073be47d64e3.png)


 4.AWS keypairs "Go to EC2 instance - Network and security : keypairs - create a key pair - It downaloads as "example.pem" (make sure pem file is downloaded in the git clonned directory)


### Installing

clone the git repository of the tool’s source code. You can install Terraform and Ansible using install.sh

```
git clone https://github.com/Bhanuvadlamudi/iac-cm

./install.sh
```

After following the getting started steps and installing terraform and ansible. Give the input of config.yaml file. 

```
vi config.yaml
```

![screenshot from 2019-02-05 22-21-35](https://user-images.githubusercontent.com/20710319/52318861-884a9a80-2994-11e9-9035-e4555c6607da.png)


## Running the script

```
./deploy.sh
```
![screenshot from 2019-02-05 22-37-39](https://user-images.githubusercontent.com/20710319/52319257-c34dcd80-2996-11e9-96ff-5d8954101b36.png)






