import requests
from requests import get
import db
from sqlalchemy.orm import sessionmaker
import json
import pandas
from urllib.request import urlopen
import db


Session = sessionmaker(bind=db.engine)  # utworzenie sesji
session = Session()


class Add_repo:
    def __init__(self, id_repo, repo_name, repo_owner):
        self.id_repo = id_repo
        self.repo_name = repo_name
        self.repo_owner = repo_owner


# zapisywanie outputu do bazy danych:
def add_repo(id_repo, repo_name, repo_owner):
    r = db.Repo(id_repo, repo_name, repo_owner)
    session.add(r)
    session.commit()


res = requests.get("https://api.github.com/repos/stencila/test").json()

# print(res['id'], res['name'], res['owner']['login'])
add_repo(res['id'], res['name'], res['owner']['login'])


#
#


def add_commit(sha, message, commited_date, author_login, author_name, author_email):
    c = db.Commit(sha, message, commited_date, author_login, author_name, author_email)
    session.add(c)
    session.commit()


with urlopen("https://api.github.com/repos/stencila/test/commits") as access_json:
    read_content = json.load(access_json)

# replies_access = data['author']
# print(replies_access)

for data in read_content:
    sha = (data['sha'])
    message = (data['commit']['message'])
    commited_date = (data['commit']['author']['date'])
    author_login = (data['author']['login'])
    author_name = (data['commit']['author']['name'])
    author_email = (data['commit']['author']['email'])

add_commit(sha, message, commited_date, author_login, author_name, author_email)


# def add_files(filename, status, changes):
#     f = db.Files(filename, status, changes)
#     session.add(f)
#     session.commit()
#
#
# with urlopen(
#         "https://api.github.com/repos/stencila/test/commits/22c0de5f9e2a4d53ae259187b16f6e9afbc53ded") as access_json:
#     read_files = json.load(access_json)
#
# # zamiana słownika na listę:
# for files in read_files['files']:
#     filename = (files['filename'])
#     status = (files['status'])
#     changes = (files['changes'])
#
# add_files(filename, status, changes)


def add_filesFromtree(file):
    tree = db.FilesFromTree(file)
    session.add(tree)
    session.commit()


with urlopen(
        "https://api.github.com/repos/stencila/test/git/trees/master?recursive=1") as access_json:
    read_files = json.load(access_json)

for file in read_files["tree"]:
    file = file['path']
    print(file)

add_filesFromtree(file)


def add_branches(name, sha):
    b = db.Branches(name, sha)
    session.add(b)
    session.commit()


with urlopen("https://api.github.com/repos/stencila/test/branches") as access_json:
    read_branches = json.load(access_json)

# zamiana słownika na listę:
for branches in read_branches:
    name = (branches['name'])
    sha = (branches['commit']['sha'])

add_branches(name, sha)


def add_pullrequests(number, state, body, commits_url):
    pull = db.PullRequests(number, state, body, commits_url)
    session.add(pull)
    session.commit()


with urlopen("https://api.github.com/repos/stencila/test/pulls?state=all") as access_json:
    read_pulls = json.load(access_json)

for pulls in read_pulls:
    number = (pulls['number'])
    state = (pulls['state'])
    body = (pulls['body'])
    commits_url = (pulls['commits_url'])

add_pullrequests(number, state, body, commits_url)

#pobieranie danych z api


# class GetRepo:
#     def __init__(self, repo_id, repo_name, repo_owner):
#         self.repo_id = repo_id
#         self.repo_name = repo_name
#         self.repo_owner = repo_owner
#
# res = requests.get(
# "https://api.github.com/repos/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE").json()
#
# g = (res['id'], res['name'], res['owner']['login'])
#
#
# class AddRepo:
#     def __init__(self, repo_id, repo_name, repo_owner):
#
# g = db.Repo(repo_id, repo_name, repo_owner)
# session.add(g)
# session.commit()
#
#
# #AddRepo(res['id'], res['name'], res['owner']['login'])
#
#
# class GetCommit:
#     def __init__(self, sha, message, commited_date, author_login, author_name, author_email):
#         self.sha = sha
#         self.message = message
#         self.commited_date = commited_date
#         self.author_login = author_login
#         self.author_name = author_name
#         self.author_email = author_email
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
# GetCommit(sha, message, commited_date, author_login, author_name, author_email)
#
#
# class AddCommit:
#     def __init__(self, sha, message, commited_date, author_login, author_name, author_email):
#
#         c = db.Commit(sha, message, commited_date, author_login, author_name, author_email)
#         session.add(c)
#         session.commit()
#
# AddCommit(sha, message, commited_date, author_login, author_name, author_email)
#
#
# class GetFiles:
#     def __init__(self, file):
#         self.file = file
#
# with urlopen(
#         "https://api.github.com/repos/stencila/test/git/trees/master?recursive=1") as access_json:
#     read_files = json.load(access_json)
#
# for file in read_files["tree"]:
#     file = file['path']
#     print(file)
#
# GetFiles(file)
#
#
# class AddFiles:
#     def __init__(self, file):
#
#         tree = db.FilesFromTree(file)
#         session.add(tree)
#         session.commit()
#
# AddFiles(file)
#
#
# class GetBranches:
#     def __init__(self, name, sha):
#         self.name = name
#         self.sha = sha
#
# with urlopen("https://api.github.com/repos/stencila/test/branches") as access_json:
#     read_branches = json.load(access_json)
#
# # zamiana słownika na listę:
# for branches in read_branches:
#      name = (branches['name'])
#      sha = (branches['commit']['sha'])
#
# GetBranches(name, sha)
#
#
# class AddBranches:
#     def __init__(self, name, sha):
#
#         b = db.Branches(name, sha)
#         session.add(b)
#         session.commit()
#
#
# AddBranches(name, sha)
#
#
# # class GetPullRequests:
# #     def __init__(self, number, state, body, commits_url):
# #         self.number = number
# #         self.state = state
# #         self.body = body
# #         self.commits_url = commits_url
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
# GetPullRequests(number, state, body, commits_url)
#
#
# class AddPullRequests:
#     def __init__(self, number, state, body, commits_url):
#
#         pull = db.PullRequests(number, state, body, commits_url)
#         session.add(pull)
#         session.commit()
#
# GetPullRequests(number, state, body, commits_url)




session.close()


#
#
# # def add_files(filename, status, changes):
# #      f = db.Files(filename, status, changes)
# #      session.add(f)
# #      session.commit()
# #
# #
# # with urlopen("https://api.github.com/repos/stencila/test/commits/22c0de5f9e2a4d53ae259187b16f6e9afbc53ded") as access_json:
# #     read_files = json.load(access_json)
# #
# #
# # #zamiana słownika na listę:
# # for files in read_files['files']:
# #     filename = (files['filename'])
# #     status = (files['status'])
# #     changes = (files['changes'])
# #
# # add_files(filename, status, changes)