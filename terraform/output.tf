output "flask-app_ip"{
	value = "${aws_instance.flask-app.public_ip}"
}
output "flask-app-prod-elb_elb_dns"{
	value = "${aws_elb.flask-app-prod-elb.dns_name}"
}
