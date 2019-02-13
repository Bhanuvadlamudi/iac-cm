import yaml
import os

ANSIBLE_FILE="./ansible/test.yaml"
SRC_DEST = "/src/testapp/"

def ansible_intialize(config):

	appConfig= config['inputs']['app']
	#print (appConfig)
	#add initialize github task
	git_task = getGitTask(appConfig['git_url'], SRC_DEST)
	app_task = getAppTask(appConfig['init_file'], SRC_DEST)
	tasks = [git_task, app_task]
	#print(yaml.safe_dump(tasks, default_flow_style=False))

	with open(ANSIBLE_FILE, 'w') as outfile:
		yaml.dump(tasks, outfile, default_flow_style=False)

def getAppTask(file_name,dest_folder):
	task={}
	task['name'] = "run flask app"
	task['become'] = "True"
	task['become_method'] = "sudo"
	task['remote_user'] ="ubuntu"
	task['shell'] = str("nohup python3 ") + str(dest_folder) + str(file_name)+" "+ str("&")
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
