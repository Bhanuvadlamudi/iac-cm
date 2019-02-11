# AuToNoMoUS

> A Tool to automate Infrastruture as Code and Configuration Management

  | Presentation: [slides](https://www.slideshare.net/BhanusreeVadlamudi/bhanusreevadlamudi?qid=79ab66f6-ceeb-4580-947a-80d11ad37123&v=&b=&from_search=1) | Contact: [linkedin](https://www.linkedin.com/in/bhanusree-vadlamudi-24903052/) |
  
  <hr/>


## About

A tool to automate the steps of provisioning of Infrastructure and Configuration Management to AWS for Flask web applications. This helps to deploy your applications with minimum knowledge of the tools for Iac and CM.

## Data Pipeline 

![gif](https://user-images.githubusercontent.com/20710319/52317884-f04ab200-298f-11e9-9b4e-d7ff4107b319.gif)


## Requriments

What you will need:

- AWS Account
- AWS Access, Secret keys. "Dont forget to download csv of your IAM". 
- Add Permissions to IAM user

  ![screenshot from 2019-02-05 21-03-58](https://user-images.githubusercontent.com/20710319/52316614-37ce3f80-298a-11e9-9884-073be47d64e3.png)


 - AWS keypairs "Go to EC2 instance - Network and security : keypairs - create a key pair - It downaloads as "example.pem" (make sure pem file is downloaded in the git clonned directory)

---
## Getting Started

### Clone

Clone this repository to your local machine using the following command:

```
git clone https://github.com/Bhanuvadlamudi/iac-cm
```
### Setup steps
1. Run the "install.sh" file which will install the requried tools for IAC (Terraform) and CM (Ansible)
```
./install.sh
```
2. Modify the "config.yaml" file as per the comments mentioned inside the file


![screenshot from 2019-02-05 22-21-35](https://user-images.githubusercontent.com/20710319/52318861-884a9a80-2994-11e9-9035-e4555c6607da.png)
---

3. Run the script "deploy.sh" which will perform all the requried steps.

```
./deploy.sh
```
![screenshot from 2019-02-05 22-37-39](https://user-images.githubusercontent.com/20710319/52319257-c34dcd80-2996-11e9-96ff-5d8954101b36.png)

---
### To delete created resources
```
./destroy.sh

```



