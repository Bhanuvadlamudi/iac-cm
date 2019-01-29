import json
from utils import terraform_util

"""
"""
def terr_intialize(config):

	#---------------adding to var.tf ------------
	key_name = config['inputs']['key_name']
	#add_variable('ssh_key',key_name)

	#-------------- adding to main.tf---------------
	#retrieving provider part
	provider = parse_provider(config['inputs']['provider'])
	#retrieving resources part
	resources = parse_resources(config['inputs']['resources'], key_name)


#def add_variable(name, value):
	


def parse_provider(pdict):
	provider = terraform_util.Provider(pdict)
	#print (provider)
	append_to_file('main1.tf', str(provider) )
	return provider

def parse_resources(resources, key_name):
	#print(resources)
	for resource in resources:
		parse_resource(resource, key_name)


def parse_resource(rdict, key_name):
	#print (rdict)
	rdict['key_name']= key_name
	resource = terraform_util.Resource(rdict)
	append_to_file('main1.tf', str(resource) )


'''
appeds given data to a file.
inputs "file_name: the file which to write, data: data to be appended"       
'''
def append_to_file(file_name, data):
	fout = open(file_name, "a")
	fout.write(data + "\n")
	fout.close()




