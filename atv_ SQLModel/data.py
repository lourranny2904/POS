import pandas as pd
from sqlmodel import SQLModel, Session, create_engine
from models import Pedido

csv_path = "20250702_Pedidos_csv_2025.csv"
db_path = "sqlite:///pedidos.db"


df = pd.read_csv(csv_path, sep=";", encoding="utf-16")


df['FormaResposta'] = df['FormaResposta'].fillna('')

df['FormaResposta'] = df['FormaResposta'].astype(str)



# Criando o banco de dados e tabelas
engine = create_engine(db_path)
SQLModel.metadata.create_all(engine)

# Inserindo os dados
with Session(engine) as session:
    for index, row in df.iterrows():
        try:
        
            pedido_data = row.to_dict()
            pedido = Pedido(**pedido_data)
            session.add(pedido)
        except Exception as e:
           
            print(f"Erro ao processar a linha {index}: {e}")
            print(f"Dados da linha: {row.to_dict()}")
            
            continue 
    

    session.commit()

print("Dados carregados com sucesso.")