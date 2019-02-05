provider "aws" {
	access_key = "AKIAIXNBKMUYYIGZPIIA"
	secret_key = "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"
	region = "us-east-1"
}
resource "aws_instance" "deploy" {
	ami = "ami-0ac019f4fcb7cb7e6"
	key_name = "hello"
	instance_type = "t2.micro"
	tags = {
		Name="deploy"
	}
	vpc_security_group_ids = ["${aws_security_group.Auto.id}"]
	connection {
		type = "ssh"
		user = "ubuntu"
		private_key = "hello.pem"
		agent =false
	}
	provisioner "local-exec" {
		command = "sleep 30; ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -v -i '${self.public_ip},' --private-key /home/bhanu/Documents/iac-cm/ansible/hello.pem /home/bhanu/Documents/iac-cm/ansible/init.yaml -e 'ansible_python_interpreter=/usr/bin/python3'"
}
}
