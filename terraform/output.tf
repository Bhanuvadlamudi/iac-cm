output "deploy_ip"{
	value = "${aws_instance.deploy.public_ip}"
}
