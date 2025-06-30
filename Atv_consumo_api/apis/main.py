from fastapi import FastAPI,HTTPException
from models import Veiculo
from typing import List


app = FastAPI()
veiculos:List[Veiculo]=[]

#listar veiculos
@app.get("/veiculos",response_model=List[Veiculo])
def listar_veiculo():
    return veiculos

#criar veiculos
@app.post("/veiculos", response_model=Veiculo)
def criar_veiculo(veiculo:Veiculo):
    veiculos.append(veiculo)
    return veiculo

#deletar veiculos
@app.delete("/veiculos/{nome}",response_model=Veiculo)
def deletar_veiculo(nome:str):
    for id, veiculo in enumerate(veiculos):
        if veiculo.nome == nome:
            veiculos.pop(id)
            return veiculo
    raise HTTPException(404,"Não localizado")