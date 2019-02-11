
class Provider:

	def __init__(self, pdict):
		self.access_key = str( pdict['access_key'])
		self.secret_key = str( pdict['secret_key'])
		self.region = str( pdict['region'])

	def __str__(self):
		return ("provider \"aws\" {" 
				+ "\n\taccess_key = \"" + self.access_key + "\""
				+ "\n\tsecret_key = \"" + self.secret_key + "\"" 
				+ "\n\tregion = \"" + self.region + "\""
				+ "\n}"
				) 

class Resource:
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
  def __init__(self,instance_name):
  	self.name = instance_name

  def __str__(self):
  	return ("output " 
				+ "\""+self.name+"_ip\"{"
				+ "\n\tvalue = \"${aws_instance." + self.name + ".public_ip}\""  
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
				+ "\n}"
			)

