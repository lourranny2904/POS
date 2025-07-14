from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Session, create_engine, select
from models import Pedido

app = FastAPI()
engine = create_engine("sqlite:///pedidos.db")

@app.get("/pedido/{id}")
def get_pedido(id: int):
    with Session(engine) as session:
        pedido = session.exec(select(Pedido).where(Pedido.IdPedido == id)).first()
        if not pedido:
            raise HTTPException(status_code=404, detail="Pedido não encontrado.")
        return pedido
