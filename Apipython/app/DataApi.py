import requests
#from numpy.lib._datasource import Repository
import sys
from requests import get
import db
from sqlalchemy.orm import sessionmaker
import json
import pandas
from urllib.request import urlopen
import db


Session = sessionmaker(bind=db.engine)
session = Session()

class GitHubApi:
    def __init__(self, repo_name, repo_owner, repo_url):
        self.__repo_name = repo_name
        self.__repo_owner = repo_owner
        self.__repo_url = repo_url

    def get_repo(self):
        repo_data = self.__get_repo_data()
        commits = self.__get_commits()
        branches = self.__get_branches()
        pulls = self.__get_pull_requests()
        files = self.__get_files()

        return (repo_data, branches, commits, pulls, files)

    def __get_commits(self):
        commits_data = self.__requests("commits")

        commits = []

        for data in commits_data:

            commits.append(db.Commit(data['sha'], data['commit']['message'], data['commit']['author']['date'], data['commit']['author']['name'], data['commit']['author']['email']))
        return commits

    def __get_branches(self):
        branches_data = self.__requests("branches")

        branches = []

        for data in branches_data:
            branches.append(db.Branches(data['name'], data['commit']['sha']))
        return branches

    def __get_pull_requests(self):
        pull_requests_data = self.__requests("pulls?state=all")

        pulls = []

        for data in pull_requests_data:
            pulls.append(db.PullRequests(data['number'], data['state'], data['body'], data['commits_url']))
        return pulls

    def __get_files(self):
        files_data = self.__requests("git/trees/master?recursive=1")
        files = []

        for data in files_data["tree"]:
            files.append(db.FilesFromTree(data['path']))

        return files



    def __get_repo_data(self):
        repo_data = [self.__repo_name, self.__repo_owner]


        repo_data = repo_data.append(db.Repo(self.__repo_name, self.__repo_owner))
        return repo_data


    def __requests(self, endpoint: str = ""):
        username = 'itUrsus'
        token = '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'
        #headers = ({'Authorization': 'access_token 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'})
        response = requests.get(f"{self.__repo_url}/{self.__repo_owner}/{self.__repo_name}/{endpoint}", auth=(username,token)).json()
        return response

    def __str__(self):
        return f"{gha.get_repo}"


class AddRepo(GitHubApi):

    def add_commit(self):
        pass

    def add_repo_data(self):
        pass

    def add_branches(self):
        pass

    def add_files(self):
        pass

    def add_pull_requests(self):
        pass




session.close()















# class AddCommit:
#     def __init__(self, sha, message, commited_date, author_login, author_name, author_email):
#
#         c = db.Commit(sha, message, commited_date, author_login, author_name, author_email)
#         session.add(c)
#         session.commit()
#
# AddCommit(sha, message, commited_date, author_login, author_name, author_email)


# if __name__ == '__main__':
#     gha = GitHubApi("My_first_repo", "itUrsus", "https://api.github.com/repos")
#
#     repo_data, branches, commits, pulls, files = gha.get_repo()
#
#     p = gha.get_repo()

    # for d in p:
    #     print(repo_data)








# with urlopen("https://api.github.com/repos/stencila/test") as access_json:
#      read_content = json.load(access_json)
#
# for data in read_content:
#
#     id_repo = ['id']
#     repo_name = ['name']
#     repo_owner = (['owner']['login'])
#
# print(data)


#
#
# def add_commit(sha, message, commited_date, author_login, author_name, author_email):

#     c = db.Commit(sha, message, commited_date, author_login, author_name, author_email)
#     session.add(c)
#     session.commit()
#
# with urlopen("https://api.github.com/repos/stencila/test/commits") as access_json:
#     read_content = json.load(access_json)
#
# for data in read_content:
#     sha = (data['sha'])
#     message = (data['commit']['message'])
#     commited_date = (data['commit']['author']['date'])
#     author_login = (data['author']['login'])
#     author_name = (data['commit']['author']['name'])
#     author_email = (data['commit']['author']['email'])
#
# add_commit(sha, message, commited_date, author_login, author_name, author_email)

#
#
# def add_files_from_tree(file):
#     tree = db.FilesFromTree(file)
#     session.add(tree)
#     session.commit()
#
#
# with urlopen(
#         "https://api.github.com/repos/stencila/test/git/trees/master?recursive=1") as access_json:
#     read_files = json.load(access_json)
#
# for file in read_files["tree"]:
#     file = file['path']
#     print(file)
#
# add_files_from_tree(file)
#
#
# def add_branches(name, sha):

#     b = db.Branches(name, sha)
#     session.add(b)
#     session.commit()
#
#
# with urlopen("https://api.github.com/repos/stencila/test/branches") as access_json:
#     read_branches = json.load(access_json)
#
# for branches in read_branches:
#     name = (branches['name'])
#     sha = (branches['commit']['sha'])
#
# add_branches(name, sha)
#
#
# def add_pullrequests(number, state, body, commits_url):

#     pull = db.PullRequests(number, state, body, commits_url)
#     session.add(pull)
#     session.commit()
#
#
# with urlopen("https://api.github.com/repos/stencila/test/pulls?state=all") as access_json:
#     read_pulls = json.load(access_json)
#
# for pulls in read_pulls:
#     number = (pulls['number'])
#     state = (pulls['state'])
#     body = (pulls['body'])
#     commits_url = (pulls['commits_url'])
#
# add_pullrequests(number, state, body, commits_url)
#
#
# AddRepo(res['id'], res['name'], res['owner']['login'])
#

# # zamiana słownika na listę:
# for branches in read_branches:
#      name = (branches['name'])
#      sha = (branches['commit']['sha'])
#
