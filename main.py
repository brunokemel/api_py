from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Schema do Pydantic (entrada/saída)
class UserCreate(BaseModel):
    nome : str
    email : str

# Criar usuário
@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(nome=user.nome, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Listar usuários
@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# Buscar usuário por ID
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(user)
    db.commit()
    return{"mensagem": "Usuário deletado com sucesso"}