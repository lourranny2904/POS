from pydantic import BaseModel
from datetime import datetime
from typing import List

class Usuario(BaseModel):
    username: str
    password: str
    data_criacao: datetime

class Livro(BaseModel):
    titulo: str
    ano: int
    edicao: int

class Biblioteca(BaseModel):
    nome: str
    acervo: List[Livro]
    usuario: List[Usuario]

class Emprestimo(BaseModel):
    usuario: Usuario
    livro: Livro
    data_emprestimo: datetime
    data_devolucao: datetime