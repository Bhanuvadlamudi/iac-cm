provider "aws" {
	profile = "iac-cm-user"
	region = "us-east-1"
}
resource "aws_instance" "flask-app-dev" {
	ami = "ami-0ac019f4fcb7cb7e6"
	key_name = "iac-cm-key"
	instance_type = "t2.micro"
	tags = {
		Name="flask-app-dev"
	}
	vpc_security_group_ids = ["${aws_security_group.Auto.id}"]
	connection {
		type = "ssh"
		user = "ubuntu"
		private_key = "iac-cm-key.pem"
		agent =false
	}
	provisioner "local-exec" {
		command = "sleep 30; ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -v -i '${self.public_ip},' --private-key /home/bhanu/Documents/iac-cm/newproj/iac-cm/ansible/iac-cm-key.pem /home/bhanu/Documents/iac-cm/newproj/iac-cm/ansible/init.yaml -e 'ansible_python_interpreter=/usr/bin/python3'"
	}
}
resource "aws_elb" "flask-app-prod-elb" {
	name = "flask-app-prod-elb"
	availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
	security_groups = ["${aws_security_group.Auto.id}"]
	health_check {
		healthy_threshold = 2
		unhealthy_threshold = 10
		timeout = 10
		interval = 60
		target = "HTTP:80/"
	}
	listener {
		lb_port = 80
		lb_protocol = "http"
		instance_port = "80"
		instance_protocol = "http"
	}
}
resource "aws_launch_configuration" "flask-app-prod-launch-config" {
	image_id = "ami-0002811a3ff2600ca"
	instance_type = "t2.micro"
	security_groups = ["${aws_security_group.Auto.id}"]
	key_name = "iac-cm-key"
	user_data = <<-EOF
							#!/bin/bash
							nohup python3 /src/testapp/test.py &
							EOF
	lifecycle {
		create_before_destroy = true
	}
}
resource "aws_autoscaling_group" "flask-app-prod-asg" {
	launch_configuration = "${aws_launch_configuration.flask-app-prod-launch-config.id}"
	availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
	min_size = 2
	max_size = 10
	desired_capacity = 3
	load_balancers = ["${aws_elb.flask-app-prod-elb.name}"]
	health_check_type = "ELB"
}
