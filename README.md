# AuToNoMoUS

> A Tool to automate Infrastruture as Code and Configuration Management

  | Presentation: [slides](https://www.slideshare.net/BhanusreeVadlamudi/bhanusreevadlamudi?qid=79ab66f6-ceeb-4580-947a-80d11ad37123&v=&b=&from_search=1) | Contact: [linkedin](https://www.linkedin.com/in/bhanusree-vadlamudi-24903052/) |
  
  <hr/>


## About

A tool to automate the steps of provisioning of Infrastructure and Configuration Management to AWS for Flask web applications. This helps to deploy your applications with minimum knowledge of the tools for Iac and CM.

- In cloud world, developers want there application to be 
   * High Availablity 
   * Fault Tolerance
   
- Most  of  the  higher-level  services,  such  as  Amazon Elastic Load Balancing (ELB),  have  been  built  with  fault  tolerance  and  high availability in mind. Services that provide basic infrastructure, such as Amazon Elastic Compute Cloud (EC2)  such as availability zones, elastic IP addresses, and snapshots, that a fault-tolerant  and  highly  available  system  must  take advantage  of  and  use  correctly.  Just  moving  a  system  into the cloud doesn’t make it fault-tolerant or highly available.

## Architecture

![tutorial_as_elb_architecture](https://user-images.githubusercontent.com/20710319/52691845-20fe8e80-2f30-11e9-8a73-50e309198a29.png)

  
## System Over View

### 1. ELB:
Load  balancing  is  an  effective  way  to  increase  the availability  of  a  system.  Instances  that  fail  can  be replaced  seamlessly  behind  the  load  balancer  while  other instances continue to operate. Elastic Load Balancing can be used to balance across instances in multiple availability  zones of a region.

### 2. Auto Scaling Group
Creates an automated, self-healing architecture that replaces failed instances and scales out with little or no human intervention requires a significant time investment upfront. 

### 3. Availability  zones  (AZs)
They are distinct  geographical locations  that  are  engineered  to  be  insulated  from failures in other AZs. By placing Amazon EC2 instances in multiple AZs, an application can be protected from failure at a single location. 



## Data Pipeline 

![gif](https://user-images.githubusercontent.com/20710319/52317884-f04ab200-298f-11e9-9b4e-d7ff4107b319.gif)


## Requriments

What you will need:

- AWS Account
- AWS Profile (Note: Do not forget to download csv file)
  * [Instructions](https://blog.gruntwork.io/authenticating-to-aws-with-the-credentials-file-d16c0fbcbf9e) for Authenticating to AWS with the Credentials File.
  
  ![screenshot from 2019-02-13 00-46-02 png](https://user-images.githubusercontent.com/20710319/52690135-a8e19a00-2f2a-11e9-8314-69bd1c7afbf1.png)

- Add Permissions to IAM user

  ![screenshot from 2019-02-05 21-03-58](https://user-images.githubusercontent.com/20710319/52316614-37ce3f80-298a-11e9-9884-073be47d64e3.png)


 - AWS keypairs "Go to EC2 instance - Network and security : keypairs - create a key pair - It downaloads as "example.pem" (make sure pem file is downloaded in the git clonned directory)
 ```
 chmod 400 example.pem
 ````

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


![screenshot from 2019-02-13 01-08-44](https://user-images.githubusercontent.com/20710319/52690554-0b876580-2f2c-11e9-968b-a9c7e2b08b69.png)

---

3. Run the script "deploy.sh" which will perform all the requried steps.

```
./deploy.sh
```

![screenshot from 2019-02-13 01-10-25](https://user-images.githubusercontent.com/20710319/52690627-4ab5b680-2f2c-11e9-8c6d-43a67d1f8be7.png)


---
### To delete created resources
```
./destroy.sh

```



