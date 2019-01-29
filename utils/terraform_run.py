import json
from utils import terraform_util
import os

MAIN_FILE = "./terraform/main.tf"
VAR_FILE  = "./terraform/variable.tf"
OUT_FILE  = "./terraform/output.tf"

"""
"""
def terr_intialize(config):

	#Remove if files exits
	delete_file(MAIN_FILE)
	delete_file(VAR_FILE)
	delete_file(OUT_FILE)


	#---------------adding to var.tf ------------
	key_name = config['inputs']['key_name']
	add_variable('ssh_key','hello.pem')
	add_variable('http_port','80')
	add_variable('ssh_port','22')

	#-------------- adding to main.tf---------------
	#retrieving provider part
	provider = parse_provider(config['inputs']['provider'])
	#retrieving resources part
	resources = parse_resources(config['inputs']['resources'], key_name)


def add_variable(name, default_value):
	variable = terraform_util.Variable({'name':name, 'default':default_value})
	#print (variable)
	append_to_file(VAR_FILE, str(variable) )

def parse_provider(pdict):
	provider = terraform_util.Provider(pdict)
	#print (provider)
	append_to_file(MAIN_FILE, str(provider) )
	return provider

def parse_resources(resources, key_name):
	#print(resources)
	for resource in resources:
		parse_resource(resource, key_name)


def parse_resource(resource, key_name):
	#print (resource)
	resource['key_name']= key_name
	resource_out = terraform_util.Resource(resource)
	append_to_file(MAIN_FILE, str(resource_out) )

	output_var = terraform_util.Output(resource['name'])
	append_to_file(OUT_FILE, str(output_var) )


'''
appeds given data to a file.
inputs "file_name: the file which to write, data: data to be appended"       
'''
def append_to_file(file_name, data):
	fout = open(file_name, "a")
	fout.write(data + "\n")
	fout.close()

def delete_file(file_name):
	if os.path.exists(file_name):
		os.remove(file_name)
	else:
		print("The file does not exist")




