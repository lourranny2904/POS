from pydantic import BaseModel
from datetime import date
from typing import List

class Veiculo(BaseModel):
    nome:str
    marca:str
    modelo:str
    placa: int
    

