from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposGeralCTe_v300 import *


class TConsStatServ(Element):
    """Tipo Pedido de Consulta do Status do Serviço CTe"""
    tpAmb: TAmb = Element(TAmb)
    xServ: TServ = Element(TServ)
    versao: str = Attribute(None)


class TVerConsStat(str):
    """Tipo Versão do Consulta do Status do Serviço CTe"""
    _restriction = Restriction(base=r"xs:string", pattern=r"3\.00", enumeration=[])
    pass


class TRetConsStatServ(Element):
    """Tipo Resultado da Consulta do Status do Serviço CTe"""
    tpAmb: TAmb = Element(TAmb)
    verAplic: str = Element(str)
    cStat: TStat = Element(TStat)
    xMotivo: TMotivo = Element(TMotivo)
    cUF: TCodUfIBGE = Element(TCodUfIBGE)
    dhRecbto: TDateTimeUTC = Element(TDateTimeUTC)
    tMed: str = Element(str, min_occurs=0)
    dhRetorno: TDateTimeUTC = Element(TDateTimeUTC, min_occurs=0)
    xObs: str = Element(str, min_occurs=0)
    versao: str = Attribute(TVerConsStat)


