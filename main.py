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
    # Verificar se o email já existe
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
            raise HTTPException(status_code=400, detail="Email já cadastrado")

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

   # Atualizar usuário
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
        # Checar duplicado no update
    email_exists = db.query(models.User).filter(
        models.User.email == user.email, 
        models.User.id != user_id
    ).first()

    if email_exists:
        raise HTTPException(status_code=400, detail="Email já cadastrado por outro usuário")

     # Atualizar os campos
    db_user.nome = user.nome
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user