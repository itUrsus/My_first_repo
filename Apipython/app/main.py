from fastapi import FastAPI, Depends
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/repositories')
def create(request: schemas.Repositories, db: Session = Depends(get_db)):
    new_repositories = models.Repositories(id_repo=request.id_repo, name=request.name, owner=request.owner)
    db.add(new_repositories)
    db.commit()
    db.refresh(new_repositories)
    return new_repositories

@app.get('/repositories')
def all(db: Session = Depends(get_db)):
    repos = db.query(models.Repositories).all()
    return repos

@app.get('/repositories/{id}')
def show(id, db: Session = Depends(get_db)):
    repo = db.query(models.Repositories).filter(models.Repositories.id == id).first()
    return repo


