# This file is main file to prepare analysis data.

from git import Repo

COMMIT = "commit "

'''
import requests
#git_url = "https://api.github.com/search/repositories"
#query = {'lat':'45', 'lon':'180'}
#response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
git_repo_url = "https://api.github.com/repos/"
response = requests.get(git_repo_url)
print(response) #response.content() # Return the raw bytes of the data payload #response.text() # Return a string representation of the data payload
print(response.json()) # This method is convenient when the API returns JSON

git_repos = {
   "Python": "https://github.com/TheAlgorithms/Python"
 , "freeCodeCamp" : "https://github.com/freeCodeCamp/freeCodeCamp"
 , "vue" : "https://github.com/vuejs/vue)"
 , "react" :"https://github.com/facebook/react"
 , "bootstrap" : "https://github.com/twbs/bootstrap"
 , "linux" : "https://github.com/torvalds/linux"
 , "tensorflow ": "https://github.com/tensorflow/tensorflow"
 , "bitcoin" : "https://github.com/bitcoin/bitcoin"
 , "angular" : "https://github.com/angular/angular"
 , "vscode" : "https://github.com/microsoft/vscode"
}

repos = []
for i in len(git_repos):
    response[i] = requests.get(git_repos[i])
'''

#git show filename from log only: git log --name-only
#def read_git_log_lines():
#    
#    try:
#        with open('./gitlog') as fs:
#            lines = fs.readlines()
#            for index, line in enumerate(lines):
#                #print("---- {}: {}".format(index, line.strip()))
#                if COMMIT in line:
#                    print("Found commit:", lines)
#    finally:
#        fs.close()
#read_git_log_lines():

REPO_PATH = "../../db_java/RoundedImageView"


import pdb

def collect_all_commits():
    all_commits = []
    repo = Repo(REPO_PATH)
    assert not repo.bare
    c = 0
    print("Commits length is:", len(list(repo.iter_commits())))
    for commit in list(repo.iter_commits()):
        all_commits.append(
            {"commit": commit.hexsha, "files": commit.stats.files})
        c = c + 1
        #print("Reached:", c, "--", commit)
    return all_commits

def collect_java_commits(allCommits):
    files = []
    for commit in allCommits:
        #print(">>>Checking:", commit)
        for c in commit["files"]:
            if "java" in c:
                #print ("-------------Found java in:", c)
                if c not in files:
                    files.append(c)
                    print (">>>>>>>>> Added java commit:", c)
    return files

# Initial point to start script
def main():
    # Parse and collect all commits as array
    all_commits = collect_all_commits()
    
    # Collect only commits with .java file changes
    java_files = collect_java_commits(all_commits)

if __name__ == "__main__":
    main()
