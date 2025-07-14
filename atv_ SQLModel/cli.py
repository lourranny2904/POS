from sqlmodel import Session, create_engine, select
from models import Pedido

engine = create_engine("sqlite:///pedidos.db")

def buscar_pedido_por_id():
    try:
        pedido_id = int(input("Digite o ID do pedido: "))
    except ValueError:
        print("ID inválido. Deve ser um número inteiro.")
        return

    with Session(engine) as session:
        # Busca o pedido pelo IdPedido
        pedido = session.exec(select(Pedido).where(Pedido.IdPedido == pedido_id)).first()
        if pedido:
            print("\nPedido encontrado:\n")
   
            print(pedido.model_dump_json(indent=2))

        else:
            print("Erro 404: Pedido não encontrado.")

if __name__ == "__main__":
    buscar_pedido_por_id()