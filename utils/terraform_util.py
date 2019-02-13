class Provider:
	def __init__(self, pdict):
		self.aws_profile = str( pdict['profile'])
		self.region = str( pdict['region'])

	def __str__(self):
		return ("provider \"aws\" {"
				+ "\n\tprofile = \"" + self.aws_profile + "\""
				+ "\n\tregion = \"" + self.region + "\""
				+ "\n}"
				)
'''
We evaluate the mode of deployment and create resources based out of itself.
If you want to just test something, use highly_available: false
'''
class Resource:
	def __init__(self, rdict, dir_path):
		self.highly_available = str(rdict['highly_available'])
		self.rdict = rdict
		self.dir_path = dir_path

	def __str__(self):
		if eval(self.highly_available):
			return str(AutoScalingGroupWithELB(self.rdict, self.dir_path))
		else:
			return str(SimpleInstance(self.rdict, self.dir_path))

class SimpleInstance:
	def __init__(self, rdict, dir_path):
		self.name = str( rdict['name'])
		self.ami = str( rdict['ami'])
		self.key_name = str( rdict['key_name'].split('.')[0])

		if ( ('instance_type' not in rdict) or 	(not rdict['instance_type'].strip())):
			self.instance_type = "t1.micro"
		else:
			self.instance_type = str( rdict['instance_type'])

		self.tags = Tags({'Name': self.name})
		self.vpc_security_group_ids = Vpc(["${aws_security_group.Auto.id}"])
		self.connection = Connection({
			                'type': "ssh",
			                'user': "ubuntu",
			                'private_key': rdict['key_name'],
			                'agent': 'false'
						  })
		self.provisioner = Provisioner( "local-exec",dir_path, rdict['key_name'] )

	def __str__(self):
		return ("resource \"aws_instance\" \""+self.name+ "\" {"
				+ "\n\tami = \"" + self.ami + "\""
				+ "\n\tkey_name = \"" + self.key_name + "\""
				+ "\n\tinstance_type = \"" + self.instance_type + "\""
				+ "\n\t"+str(self.tags)
				+ "\n\t"+str(self.vpc_security_group_ids)
				+ "\n\t"+str(self.connection)
				+ "\n\t"+str(self.provisioner)
				+ "\n}"
				)

class AutoScalingGroupWithELB:
	def __init__(self, rdict, dir_path):
		self.rdict = rdict
		self.name = str( rdict['name'])
		self.ami = str( rdict['ami'])
		self.key_name = str( rdict['key_name'].split('.')[0])

		if ( ('instance_type' not in rdict) or 	(not rdict['instance_type'].strip())):
			self.instance_type = "t1.micro"
		else:
			self.instance_type = str(rdict['instance_type'])

		self.tags = Tags({'Name': self.name})
		self.vpc_security_group_ids = Vpc(["${aws_security_group.Auto.id}"])
		self.connection = Connection({
			                'type': "ssh",
			                'user': "ubuntu",
			                'private_key': rdict['key_name'],
			                'agent': 'false'
						  })

	def __str__(self):
		return (str(ELB(self.rdict))
		       + "\n" + str(LaunchConfiguration(self.rdict))
			   + "\n" + str(AutoScalingGroup(self.rdict))
			    )

class AutoScalingGroup:
	def __init__(self,rdict):
		self.asg_name = str( rdict['name'])+"-asg"
		self.elb_name = str( rdict['name'])+"-elb"
		self.launch_config_name = str( rdict['name'])+"-launch-config"
		self.availability_zones = "availability_zones = [" + "\"us-east-1a\", \"us-east-1b\", \"us-east-1c\"]"
		self.launch_configuration = "launch_configuration = \"${aws_launch_configuration." + str(self.launch_config_name) + ".id}\""
		self.load_balancers = "load_balancers = [" + "\"${aws_elb." + str(self.elb_name) + ".name}\"]"

	def __str__(self):
		return ("resource \"aws_autoscaling_group\" \""+self.asg_name+ "\" {"
				+ "\n\t"+str(self.launch_configuration)
				+ "\n\t"+str(self.availability_zones)
				+ "\n\tmin_size = 2"
				+ "\n\tmax_size = 10"
				+ "\n\tdesired_capacity = 3"
				+ "\n\t"+str(self.load_balancers)
				+ "\n\thealth_check_type = \"ELB\""
				+ "\n}"
				)

class LaunchConfiguration:
	def __init__(self,rdict):
		self.elb_name = str( rdict['name'])+"-elb"
		self.launch_config_name = str( rdict['name'])+"-launch-config"
		self.ami = str( rdict['ami'])
		self.security_groups = "security_groups = [" + "\"${aws_security_group.Auto.id}\"]"
		self.key_name = str( rdict['key_name'].split('.')[0])

		if ( ('instance_type' not in rdict) or 	(not rdict['instance_type'].strip())):
			self.instance_type = "t1.micro"
		else:
			self.instance_type = str( rdict['instance_type'])
		self.user_data = ("user_data = <<-EOF"
	                                   + "\n\t\t\t\t\t\t\t#!/bin/bash"
									   + "\n\t\t\t\t\t\t\tnohup python3 /src/testapp/test.py &"
									   + "\n\t\t\t\t\t\t\tEOF"
						  )
		self.lifecycle = ("lifecycle {"
		                  + "\n\t\tcreate_before_destroy = true"
						  + "\n\t}"
		                  )

	def __str__(self):
		return ("resource \"aws_launch_configuration\" \""+self.launch_config_name+ "\" {"
				+ "\n\timage_id = \"" + self.ami + "\""
				+ "\n\tinstance_type = \"" + self.instance_type + "\""
				+ "\n\t"+str(self.security_groups)
				+ "\n\tkey_name = \"" + self.key_name + "\""
				+ "\n\t"+str(self.user_data)
				+ "\n\t"+str(self.lifecycle)
				+ "\n}"
				)

class ELB:
	def __init__(self,rdict):
		self.name = str( rdict['name'])+"-elb"
		self.security_groups = "security_groups = [" + "\"${aws_security_group.Auto.id}\"]"
		self.availability_zones = "availability_zones = [" + "\"us-east-1a\", \"us-east-1b\", \"us-east-1c\"]"
		self.health_check = ("health_check {"
		                     + "\n\t\thealthy_threshold = 2"
							 + "\n\t\tunhealthy_threshold = 10"
							 + "\n\t\ttimeout = 10"
							 + "\n\t\tinterval = 60"
							 + "\n\t\ttarget = \"HTTP:80/\""
							 + "\n\t}"
							 )
		self.listener = ("listener {"
		                     + "\n\t\tlb_port = 80"
							 + "\n\t\tlb_protocol = \"http\""
							 + "\n\t\tinstance_port = \"80\""
							 + "\n\t\tinstance_protocol = \"http\""
							 + "\n\t}"
							 )

	def __str__(self):
		return ("resource \"aws_elb\" \""+self.name+ "\" {"
				+ "\n\tname = \"" + self.name + "\""
				+ "\n\t"+str(self.availability_zones)
				+ "\n\t"+str(self.security_groups)
				+ "\n\t"+str(self.health_check)
				+ "\n\t"+str(self.listener)
				+ "\n}"
				)

class Tags:
	def __init__(self,tdict):
		self.Name= str(tdict['Name'])

	def __str__(self):
		return "tags = {"+ "\n\t\tName=\""+ self.Name+"\"" +"\n\t}"

class Connection:
	def __init__(self,cdict):
		self.type = str( cdict['type'])
		self.user = str( cdict['user'])
		self.private_key = str( cdict['private_key'])
		self.agent = str(cdict['agent'])

	def __str__(self):
		return ("connection {"
				+ "\n\t\ttype = \"" + self.type + "\""
				+ "\n\t\tuser = \"" + self.user + "\""
				+ "\n\t\tprivate_key = \"" + self.private_key + "\""
				+ "\n\t\tagent ="  + str(self.agent)
				+ "\n\t}"
				)

class Vpc:
	def __init__(self,ids):
		self.ids = ids

	def __str__(self):
		output = "vpc_security_group_ids = ["
		for id in self.ids:
			output = output + "\""+ str(id) + "\","
		output = output[:-1]
		output = output+ "]"
		return output

class Variable:
  def __init__(self,vdict):
  	self.name = vdict['name']
  	self.default = vdict['default']

  def __str__(self):
  	return ("variable "
				+ "\""+self.name+"\"{"
				+ "\n\tdefault = \"" + self.default + "\""
				+ "\n}"
			)

class Output:
  def __init__(self,rdict):
	  self.name = str(rdict['name'])
	  self.highly_available = str(rdict['highly_available'])

  def __str__(self):
	  if eval(self.highly_available):
		  return str(ELBOutput(self.name+"-elb"))
	  else:
		  return str(EC2Output(self.name))

class EC2Output:
  def __init__(self,instance_name):
  	self.name = instance_name

  def __str__(self):
  	return ("output "
				+ "\""+self.name+"_ip\"{"
				+ "\n\tvalue = \"${aws_instance." + self.name + ".public_ip}\""
				+ "\n}"
			)

class ELBOutput:
  def __init__(self,elb_name):
  	self.name = elb_name

  def __str__(self):
  	return ("output "
				+ "\""+self.name+"_elb_dns\"{"
				+ "\n\tvalue = \"${aws_elb." + self.name + ".dns_name}\""
				+ "\n}"
			)

class Provisioner:
  def __init__(self, name, dir_path, key_name):
  	self.name = name
  	self.dir_path = dir_path
  	self.key_name = key_name

  def __str__(self):
  	return ("provisioner "
				+ "\""+self.name+"\" {"
				+ "\n\t\tcommand = \"sleep 30; ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -v -i '${self.public_ip},' --private-key " + self.dir_path + "/ansible/"+ self.key_name + " " + self.dir_path +  "/ansible/init.yaml -e 'ansible_python_interpreter=/usr/bin/python3'\""
				+ "\n\t}"
			)
