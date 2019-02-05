import yaml
from utils import terraform_run
from utils import ansible_init
import os


def load_yaml(file):
	with open(file, 'r') as f:
		config = yaml.safe_load(f)
		#print (config)
		return config

def main():
	
	dir_path = (os.getcwd())
	# load the yaml config file
	config = load_yaml('./config.yaml')

	#finalize terraform scripts
	terraform_run.terr_intialize(config, dir_path)

	#finalize ansible scripts
	ansible_init.ansible_intialize(config)



if __name__ == "__main__": main()



