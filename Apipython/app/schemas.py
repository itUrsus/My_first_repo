from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Repositories(BaseModel):
    id_repo: int
    name: str
    owner: str
