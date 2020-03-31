from hecuba import *
from pydantic import BaseModel


class IPlogs(StorageDict):
    '''
    @TypeSpec dict<<FK_NUMPERSO:int, PK_ANYOMESDIA:str>, IP_TERMINAL:str, FK_COD_OPERACION:str>
    '''
    pass


class IPlogJSON(BaseModel):
    FK_NUMPERSO: int
    PK_ANYOMESDIA: str
    IP_TERMINAL: str
    FK_COD_OPERACION:  str

