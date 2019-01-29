import yaml
from utils import terraform_run


def load_yaml(file):
	with open(file, 'r') as f:
		config = yaml.safe_load(f)
		print (config)
		return config

def main():
	# load the yaml config file
	config = load_yaml('./config.yaml')

	#finalize terraform scripts
	terraform_run.terr_intialize(config)

	#finalize ansible scripts

	#invoke terraform script

	#valid terraform output

	#invoke ansible scripts

if __name__ == "__main__": main()



