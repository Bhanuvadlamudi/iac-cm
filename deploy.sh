
#cd terraform
#terraform destroy

#executing the terraform 
#install.sh

echo "initializing scripts"
python3 run.py


echo "started provisioning the infrastructure"
cd terraform 
terraform init
terraform validate
echo "validated"
terraform plan
terraform apply -auto-approve 

echo "success provisioning the infrastructure"
terraform output

echo "started configuring the infrastructure"

#cd /home/bhanu/Documents/iac-cm/ansible


#ansible-playbook -v init.yaml --private-key ./hello.pem 






