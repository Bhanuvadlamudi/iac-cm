output "flask-app-dev_ip"{
	value = "${aws_instance.flask-app-dev.public_ip}"
}
output "flask-app-prod-elb_elb_dns"{
	value = "${aws_elb.flask-app-prod-elb.dns_name}"
}
