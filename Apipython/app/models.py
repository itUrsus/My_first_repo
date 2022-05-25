from sqlalchemy import Column, Integer, String
from database import Base


class Repositories(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True, index=True)
    id_repo = Column(Integer)
    name = Column(String)
    owner = Column(String)