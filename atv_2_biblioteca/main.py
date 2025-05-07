# pip install fastapi uvicorn pydantic
# pip freeze > requirements.txt
# uvicorn main:app
from fastapi import FastAPI,HTTPException
from models import Usuario, Livro, Biblioteca, Emprestimo
from typing import List

app = FastAPI()

usuarios: List[Usuario] = []
livros: List[Livro] = []
bibliotecas: List[Biblioteca] = []
emprestimos: List[Emprestimo] = []

# APIs para usuario
@app.get("/usuarios/", response_model=List[Usuario])
def listar_usuarios():
    return usuarios

@app.post("/usuarios/", response_model=Usuario)
def criar_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return usuario

@app.delete("/usuarios/{username}", response_model=Usuario)
def excluir_usuario(username: str):
    for index, usuario in enumerate(usuarios):
        if usuario.username == username:
            return usuarios.pop(index)
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# APIs para livros

@app.get("/livros/", response_model=List[Livro])
def listar_livros():
    return livros

@app.post("/livros/", response_model=Livro)
def criar_livros(livro: Livro):
    livros.append(livro)
    return livro

@app.delete("/livros/{titulo}", response_model=Livro)
def excluir_livro(titulo: str):
    for index, livro in enumerate(livros):
        if livro.titulo == titulo:
            return livros.pop(index)
    raise HTTPException(status_code=404, detail="Livro não encontrado")

# APIs para biblioteca

@app.get("/bibliotecas/", response_model=List[Biblioteca])
def listar_bibliotecas():
    return bibliotecas


@app.post("/bibliotecas/", response_model=Biblioteca)
def criar_biblioteca(biblioteca: Biblioteca):
    bibliotecas.append(biblioteca)
    return biblioteca

@app.delete("/bibliotecas/{nome}", response_model=Biblioteca)
def excluir_biblioteca(nome: str):
    for index, biblioteca in enumerate(bibliotecas):
        if biblioteca.nome == nome:
            return bibliotecas.pop(index)
    raise HTTPException(status_code=404, detail="Biblioteca não encontrada")

# APIs para emprestimos

@app.get("/emprestimos/", response_model=List[Emprestimo])
def listar_emprestimos():
    return emprestimos

@app.post("/emprestimos/", response_model=Emprestimo)
def criar_emprestimos(emprestimo: Emprestimo):
    emprestimos.append(emprestimo)
    return emprestimo

@app.delete("/emprestimos/{usuario_username}/{livro_titulo}", response_model=Emprestimo)
def excluir_emprestimo(usuario_username: str, livro_titulo: str):
    for index, emprestimo in enumerate(emprestimos):
        if emprestimo.usuario.username == usuario_username and emprestimo.livro.titulo == livro_titulo:
            return emprestimos.pop(index)
    raise HTTPException(status_code=404, detail="Empréstimo não encontrado")

# Para depuração
@app.get("/")
def read_root():
    return {"message": "API de Biblioteca funcionando!"}

