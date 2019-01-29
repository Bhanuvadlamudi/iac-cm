provider "aws" {
aws_access_key = ""
aws_secret_key = ""
region = "${var.region}"
}

resource "aws_instance" "Auto" {
  ami = "ami-0ac019f4fcb7cb7e6"
  key_name = "terr"
  instance_type = "t2.micro"  
  tags = {
    Name = "Auto"
  }

  vpc_security_group_ids = ["${aws_security_group.Auto.id}"]
  connection {
  
   type = "ssh"
   user = "ubuntu"
   private_key = "${file(var.ssh_key)}"
   agent = false

  }

  provisioner "local-exec" {
  
   command  = "sleep 30; ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -v -i '${self.public_ip},' --private-key /home/bhanu/terraform/auto/terr.pem /home/bhanu/terraform/auto/an.yaml -e 'ansible_python_interpreter=/usr/bin/python3'"
   }

}





