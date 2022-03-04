# This file is main file to prepare analysis data.

from git import Repo
import json

COMMIT = "commit "
REPO_PATH = "../../../db/android-viewbadger"

import pdb

def collect_all_commits():
    all_commits = []
    repo = Repo(REPO_PATH)
    assert not repo.bare
    c = 0
    print("All commits length is:", len(list(repo.iter_commits())))
    for commit in list(repo.iter_commits()):
        all_commits.append(
            {"commit": commit.hexsha, "files": commit.stats.files})
        c = c + 1
    return all_commits

def collect_java_commits(allCommits):
    file_count = 0
    Acount = 0
    java_commits = {}
    for commitSet in allCommits:
        Acount = Acount + 1
        for filename in commitSet["files"]:
            file_count = file_count + 1
            if "java" in filename:
                key = commitSet["commit"]
                if key not in java_commits:
                    java_commits[key] = [filename]
                else:
                    java_commits[key].append(filename)
    print("Only java commits length is:", len(java_commits))
    return java_commits

def prepare_collection_json():
    return {"repo": {}}

# Initial point to start script
def main():
    # Prepare results statistics json format
    resultsJson = prepare_collection_json()
    # Parse and collect all commits as array
    # TODO: Add fo rl oop for collecting all repos commits
    all_commits = collect_all_commits()
    # Collect only commits with .java file changes
    java_commits = collect_java_commits(all_commits)
    name = REPO_PATH.split("/")[len(REPO_PATH.split("/")) - 1]
    resultsJson["repo"][name] = java_commits
    print("Final results json is:", resultsJson)

if __name__ == "__main__":
    main()
