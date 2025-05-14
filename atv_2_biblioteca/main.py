# pip install fastapi uvicorn pydantic
# pip freeze > requirements.txt
# uvicorn main:app
from fastapi import FastAPI,HTTPException
from models import Usuario,Livro,Biblioteca,Emprestimo
from typing import List
import datetime

app = FastAPI()


bibliotecas: List[Biblioteca] = []

@app.get("/bibliotecas",response_model=List[Biblioteca])
def listar_bibliotecas():
    return bibliotecas

@app.get("/bibliotecas/{nome}",response_model=Biblioteca)
def listar_biblioteca(nome_biblioteca:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome ==nome_biblioteca:
            return biblioteca
    raise HTTPException(404,"Não localizado.")

@app.post("/bibliotecas")
def cadastrar_biblioteca(nome_biblioteca:str):
    data = {
        "nome":nome_biblioteca,
        "acervo":[],
        "usuarios":[],
        "emprestimos":[]
    }
    biblioteca = Biblioteca(**data)
    bibliotecas.append(biblioteca)
    
@app.delete("/bibliotecas/{nome}",response_model=Biblioteca)
def listar_biblioteca(nome_biblioteca:str):
    for id,biblioteca in enumerate(bibliotecas):
        if biblioteca.nome == nome_biblioteca:
            bibliotecas.pop(id)
            return biblioteca
    raise HTTPException(404,"Não localizado.")

@app.get("/usuarios/",response_model=List[Usuario])
def listar_usuarios(nome_usuario:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_usuario:
            return biblioteca.usuarios
    raise HTTPException(404,"Não localizado.")

@app.get("/usuarios/{username}", response_model=Usuario)
def listar_usuario(nome_usuario:str, username:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_usuario:
            for usuario in biblioteca.usuarios:
                if usuario.username == username:
                    return usuario
    raise HTTPException(404,"Usuário não localizado")

@app.post("/usuarios/")
def criar_usuario(nome_usuario:str,usuario:Usuario):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_usuario:
            return biblioteca.usuarios.append(usuario)
    raise HTTPException(404,"Não localizado.")
   
@app.delete("/usuarios/{username}",response_model=Usuario)
def excluir_usuario(nome_usuario:str,username:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_usuario:
            for id,usuario in enumerate(biblioteca.usuarios):
                if usuario.username == username:
                    biblioteca.usuarios.pop(id)
                    return usuario
    raise HTTPException(404,"Usuário não localizado")

@app.get("/livros",response_model=List[Livro])
def listar_livros(nome_livros:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_livros:
            return biblioteca.acervo
    raise HTTPException(404,"não localizado")  
 
@app.get("/livros/{titulo}",response_model=Livro)
def listar_livros(nome_livros:str, titulo:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_livros:
            for livro in biblioteca.acervo:
             if livro.titulo == titulo:
                return livro
    raise HTTPException(404,"Não localizado")

@app.delete("/livros/{titulo}",response_model=Livro)
def deletar_livro(nome_livros:str,titulo:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_livros:
            for id, livro in enumerate(biblioteca.acervo):
                if livro.titutlo == titulo:
                    biblioteca.acervo.pop(id)
                    return livro
    raise HTTPException(404,"Não localizado")

@app.post("/livros", response_model=Livro)
def criar_livro(nome_livros:str,livro:Livro):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_livros:
            biblioteca.acervo.append(livro)
            return livro
    raise HTTPException(404,"Não localizado")

@app.get("/emprestimos",response_model=List[Emprestimo])
def listar_emprestimos(nome_emprestimo:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_emprestimo:
            return biblioteca.emprestimos
    raise HTTPException(404,"Não localizado")

@app.post("/emprestimos")
def cadastrar_emprestimos(nome_emprestimo:str,usuario:str,titulo:str):
    user = None
    book = None
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_emprestimo:
            for u in biblioteca.usuarios:
                if u.username == usuario:
                    user = u
            for l in biblioteca.acervo:
                if l.titulo == titulo:
                    book = l
            if user and book:
                data = {
                    "usuario":user,
                    "livro":book,
                    "data_emprestimo":datetime.datetime.now().date(),
                    "data_devolucao":datetime.date(2025,5,31),
                }
                emprestimo = Emprestimo(**data)
                biblioteca.emprestimos.append(emprestimo)
    if not user or not book:
        raise HTTPException(404,"Não localizado")