

echo "initializing scripts"
python3 run.py


echo "started provisioning the infrastructure"
cd terraform 
terraform init
terraform validate
echo  "********* validated **********"
terraform plan
terraform apply -auto-approve 

echo "success provisioning the infrastructure"
terraform output



