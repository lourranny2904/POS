# pip install fastapi uvicorn pydantic
# pip freeze > requirements.txt
# uvicorn main:app
from fastapi import FastAPI,HTTPException
from models import Carro, Cliente, Reserva
from typing import List

app = FastAPI()

carros: List[Carro] = []
clientes: List[Cliente] = []
reservas: List[Reserva] = []


# APIs para carro
@app.get("/carros/", response_model=List[Carro])
def listar_Carros():
    return carros

@app.post("/carros/", response_model=Carro)
def add_carro(carro: Carro):
    carros.append(carro)
    return carro

@app.delete("/carros/{id}", response_model=Carro)
def excluir_carro(id: int):
    for index, carro in enumerate(carros):
        if carro.id == id:
            return carros.pop(index)
    raise HTTPException(status_code=404, detail="carro não encontrado")

@app.put("/carros/{id}", response_model=Carro)
def atualizar_carro(id: int, carro_atualizado: Carro):
    for index, carro in enumerate(carros):
        if carro.id == id:
            carros[index] = carro_atualizado
            return carro_atualizado
    raise HTTPException(status_code=404, detail="Carro não encontrado")

#APIs para cliente

@app.get("/clientes/", response_model=List[Cliente])
def listar_cliente():
    return clientes

@app.post("/clientes", response_model=Cliente)
def adicionar_cliente(cliente: Cliente):
    clientes.append(cliente)
    return cliente

@app.get("/clientes/{id}", response_model=Cliente)
def buscar_cliente(id: int):
    for cliente in clientes:
        if cliente.id == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

#APIs para reservas 


@app.get("/reservas/", response_model=Reserva)
def listar_reserva():
    return reservas

@app.post("/reservas", response_model=Reserva)
def criar_reserva(reserva: Reserva):
    for i, carro in enumerate(carros):
        if carro.id == reserva.carro.id:
            if not carro.disponivel:
                raise HTTPException(status_code=400, detail="Carro indisponível")
            carros[i].disponivel = False
            reservas.append(reserva)
            return reserva
    raise HTTPException(status_code=404, detail="Carro não encontrado")

@app.delete("/reservas/{id}")
def cancelar_reserva(id: int):
    for i, reserva in enumerate(reservas):
        if reserva.id == id:
            for carro in carros:
                if carro.id == reserva.carro.id:
                    carro.disponivel = True
                    break
            del reservas[i]
            return {"mensagem": "Reserva cancelada com sucesso"}
    raise HTTPException(status_code=404, detail="Reserva não encontrada")


