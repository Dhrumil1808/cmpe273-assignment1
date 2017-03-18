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
    repo = git.get_repo(git_repo);
    content = repo.get_file_contents(filename.split('.')[0] +'.yml')
    #content=content.decoded_content
    if  filename.endswith('.yml'):
        with open(filename,'r') as yml:
        	data=yml.read().replace('\n','')
        	return data
    elif filename.endswith('.json'):
        return json.dumps(yaml.load(content.decoded_content),sort_keys=False, indent=2)
        

if __name__ == "__main__":
	for arg in sys.argv:
		print arg
	git_repo = arg.replace('https://github.com/','')
	#print git_repo
	app.run(debug=True,host='0.0.0.0')