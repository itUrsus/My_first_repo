from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


#connect with database

engine = create_engine('sqlite:///app.db')
base = declarative_base()

class Repo(base):
    __tablename__ = 'repositories'

    id = Column(Integer, primary_key=True, index=True)
    id_repo = Column(Integer)
    timestamp = Column(DateTime)
    repo_name = Column(String)
    repo_owner = Column(String)


    def __init__(self, id_repo, repo_name, repo_owner):

        self.id_repo = id_repo
        self.repo_name = repo_name
        self.repo_owner = repo_owner
        self.timestamp = datetime.now()


class Commit(base):
    __tablename__ = 'commits'

    id = Column(Integer, primary_key=True, index=True)
    sha = Column(Integer)
    message = Column(String)
    commited_date = Column(String)
    author_login = Column(String)
    author_name = Column(String)
    author_email = Column(String)

    # date = Column(DateTime)

    def __init__(self, sha, message, commited_date, author_login, author_name, author_email):

        self.sha = sha
        self.message = message
        self.commited_date = commited_date
        self.author_login = author_login
        self.author_name = author_name
        self.author_email = author_email

# class Files(base):
#     __tablename__ = 'files'
#
#     id = Column(Integer, primary_key=True, index=True)
#     filename = Column(String)
#     status = Column(String)
#     changes = Column(String)
#
#     def __init__(self, filename, status, changes):
#         self.filename = filename
#         self.status = status
#         self.changes = changes


class FilesFromTree(base):
    __tablename__ = 'filesfromtree'

    id = Column(Integer, primary_key=True, index=True)
    file = Column(String)

    def __init__(self, file):
        self.file = file


class Branches(base):
    __tablename__ = 'branches'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sha = Column(String)


    def __init__(self, name, sha):
        self.name = name
        self.sha = sha


class PullRequests(base):
    __tablename__ = 'pull_requests'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    state = Column(String)
    body = Column(String)
    commits_url = Column(String)


    def __init__(self, number, state, body, commits_url):
        self.number = number
        self.state = state
        self.body = body
        self.commits_url = commits_url



base.metadata.create_all(engine)
