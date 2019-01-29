provider "aws" {
	aws_access_key_id = "a235rgfeded123"
	aws_security_key_id = " dfbjkbfjkbf"
	region = "jdfhwuf"
}
resource "aws_instance" "hellooo" {
	ami = "2jh2h"
	key_name = "key.pem"
	instance_type = "t1.micro"
	tags = {
		Name="hellooo"
	}
	connection {
		type = "ssh"
		user = "ubuntu"
		private_key = "${file(var.ssh_key)}"
		agent =false
	}
	provisioner "local-exec" {
	command = "test1"
	}
}
