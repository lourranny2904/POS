from sqlmodel import SQLModel, Field
from typing import Optional

class Pedido(SQLModel, table=True):
    IdPedido: int = Field(primary_key=True)
    ProtocoloPedido: str
    Esfera: str
    UF: Optional[str] = None
    Municipio: Optional[str] = None
    OrgaoDestinatario: str
    Situacao: str
    DataRegistro: str
    PrazoAtendimento: str
    FoiProrrogado: str
    FoiReencaminhado: str
    FormaResposta: str
    OrigemSolicitacao: str
    IdSolicitante: int
    AssuntoPedido: str
    SubAssuntoPedido: str
    Tag: Optional[str] = None
    DataResposta: Optional[str] = None
    Decisao: Optional[str] = None
    EspecificacaoDecisao: Optional[str] = None
