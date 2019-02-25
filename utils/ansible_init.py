import yaml
import os

ANSIBLE_FILE="./ansible/test.yaml"
SRC_DEST = "/src/smarthotels/"

def ansible_intialize(config):

	appConfig= config['inputs']['app']
	#print (appConfig)
	#add initialize github task
	git_task = getGitTask(appConfig['git_url'], SRC_DEST)
	app_task = getAppTask(appConfig['init_file'], SRC_DEST)
	ngix_task = getNginx()
	pip_task = getPipTask()
	spacy_task = getSpacy()
	nltk_task = getNltk()
	tasks = [git_task, ngix_task , pip_task \
	 ,spacy_task , nltk_task ,app_task]
	#print(yaml.safe_dump(tasks, default_flow_style=False))

	with open(ANSIBLE_FILE, 'w') as outfile:
		yaml.dump(tasks, outfile, default_flow_style=False)

def getAppTask(file_name,dest_folder):
	task={}
	task['name'] = "run flask app"
	task['become'] = "True"
	task['become_method'] = "sudo"
	task['remote_user'] ="ubuntu"
	task['shell'] = str("nohup python ") + str(dest_folder) + str(file_name)+" "+ str(">")+" "+ str("/usr/local/share/iac-cm.out") +" "+ str("&")
	return task

def getGitTask(repo_url, dest_folder):
	task= {}
	task['name'] = "clone git repository"
	task['git']  = getGit(repo_url, dest_folder)
	return task

def getGit(repo_url, dest_folder):
	git = {}
	git['dest'] 	= dest_folder
	git['repo'] 	= repo_url
	git['update']	= "no"
	git['version']	= "master"
	git['clone']	= "yes"
	git['accept_hostkey'] = "yes"
	return git

def getNginx():
	nginx={}
	nginx['name']	= "Configure nginx"
	nginx['include_tasks']	= "nginx.yaml"
	return nginx

def getPip():
	pip= {}
	pip['requirements']	= "/src/smarthotels/application/requirements.txt"
	return pip 

def getPipTask():
	task = {}
	task['pip'] = getPip()
	task['name'] = "req"
	task['become'] = "True"
	task['become_method'] = "sudo"
	task['remote_user'] ="ubuntu"
	return task

def getSpacy():
	spacy={}
	spacy['name']	= "spacy en"
	spacy['raw']	= "nohup python -m spacy download en &"
	spacy['become_method']	= "sudo"
	spacy['become']	= "True"
	spacy['remote_user']	= "ubuntu"
	return spacy

def getNltk():
	nltk={}
	nltk['name']	= "nltk"
	nltk['raw']	= "nohup python -m nltk.downloader vader_lexicon -d /usr/local/share/nltk_data" + str("&")
	nltk['become_method']	= "sudo"
	nltk['become']	= "True"
	nltk['remote_user']	= "ubuntu"
	return nltk
