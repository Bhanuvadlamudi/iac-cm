
class Provider:

	def __init__(self, pdict):
		self.aws_access_key_id = str( pdict['aws_access_key_id'])
		self.aws_security_key_id = str( pdict['aws_security_key_id'])
		self.region = str( pdict['region'])

	def __str__(self):
		return ("provider \"aws\" {" 
				+ "\n\taws_access_key_id = \"" + self.aws_access_key_id + "\""
				+ "\n\taws_security_key_id = \"" + self.aws_security_key_id + "\"" 
				+ "\n\tregion = \"" + self.region + "\""
				+ "\n}"
				) 

class Resource:
	def __init__(self, rdict):
		self.name = str( rdict['name'])
		self.ami = str( rdict['ami'])
		self.key_name = str( rdict['key_name'])

		if ( ('instance_type' not in rdict) or 	(not rdict['instance_type'].strip())):
			self.instance_type = "t1.micro"
		else:
			self.instance_type = str( rdict['instance_type'])

		self.tags = Tags({'Name': self.name})
		self.vpc_security_group_ids = Vpc(["${aws_security_group.Auto.id}"])
		self.connection = Connection({
			                'type': "ssh",
			                'user': "ubuntu",
			                'private_key': 'file(var.ssh_key)',
			                'agent': "false" 
						  })
		self.provisioner = Provisioner( {'command':"test1"} )

	def __str__(self):
		return ("resource \"aws_instance\" \""+self.name+ "\" {" 
				+ "\n\tami = \"" + self.ami + "\""
				+ "\n\tkey_name = \"" + self.key_name + "\"" 
				+ "\n\tinstance_type = \"" + self.instance_type + "\""
				+ "\n\t"+str(self.tags)
				+ "\n\t"+str(self.vpc_security_group_ids)
				+ "\n\t"+str(self.connection)
				#+ "\n\t"+str(self.provisioner)
				+ "\n}"
				) 

class Provisioner:
	def __init__(self,pdict):
		self.command=str(pdict['command'])

	def __str__(self):
		return ("provisioner \"local-exec\" {"
			+ "\n\tcommand = \"" + str(self.command) + "\""
			+ "\n\t}")


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
				+ "\n\t\tprivate_key = \"${" + self.private_key + "}\""
				+ "\n\t\tagent ="  + str(self.agent)  
				+ "\n\t}"
				) 


class Vpc:
	def __init__(self,ids):
		self.ids = ids

	def __str__(self):
		return "vpc_security_group_ids = "+ str(self.ids)




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

