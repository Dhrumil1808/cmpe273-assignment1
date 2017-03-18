from flask import Flask
from github import Github
import sys
import json
import yaml

git_repo=''

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/<filename>")
def getConfig(filename):
    git = Github()
    
    user=git_repo.split('/')[0]
    repositories=git_repo.split('/')[1]

    	#repos=git.get_user(user).get_repos(repositories)
    for repos in git.get_user(user).get_repos(repositories):
		if repos.name == repositories:
			repository = repos.name
			finalRepo = repos
			print repos.name
    
    content = finalRepo.get_file_contents(filename.split('.')[0] +'.yml')
    #content=content.decoded_content
    if  filename.endswith('.yml'):
        return content.decoded_content
    elif filename.endswith('.json'):
        return json.dumps(yaml.load(content.decoded_content),sort_keys=False, indent=2)
        

if __name__ == "__main__":
	for arg in sys.argv:
		print arg
	git_repo = arg.replace('https://github.com/','')
	#print git_repo
	app.run(debug=True,host='0.0.0.0')