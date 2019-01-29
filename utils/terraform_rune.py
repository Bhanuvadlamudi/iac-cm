import json
from utils import terraform_util

"""
"""
def terr_execute(config):

	#---------------adding to var.tf ------------

	#add_variable('ssh_key',key_name)

	#-------------- adding to main.tf---------------
	#retrieving provider part
	provider = parse_provider(config['inputs']['provider'])
	#retrieving resources part
	resource = parse_resource(config['inputs']['resource'])


#def add_variable(name, value):
	


def parse_provider(pdict):
	provider = terraform_util.Provider(pdict)
	#print (provider)
	append_to_file('main1.tf', str(provider) )
	return provider

#def parse_resources(rdict):
	#print(resources)
	

def parse_resource(rdict):
	#print (rdict)
	#rdict['key_name']= key_name
	resource = terraform_util.Resource(rdict)
	append_to_file('main1.tf', str(resource) )

#def parse_vpc_security_group_ids(vdict):
#	vpc_security_group_ids = terraform_util.Vpc(vdict)
#	append_to_file('main1.tf', str(vpc_security_group_ids) )


'''
appeds given data to a file.
inputs "file_name: the file which to write, data: data to be appended"       
'''
def append_to_file(file_name, data):
	fout = open(file_name, "a")
	fout.write(data + "\n")
	fout.close()




