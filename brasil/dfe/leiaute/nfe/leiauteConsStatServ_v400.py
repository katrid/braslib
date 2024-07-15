# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: leiauteConsStatServ_v4.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposBasico_v400 import *


class TVerConsStatServ(str):
    """Tipo versão do leiuate da Consulta Status do Serviço 4.00"""
    pass


class TConsStatServ(ComplexType):
    """Tipo Pedido de Consulta do Status do Serviço"""
    versao: Annotated[TVerConsStatServ, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    cUF: Annotated[TCodUfIBGE, Element] = None
    xServ: Annotated[TServ, Element] = None


class TRetConsStatServ(ComplexType):
    """Tipo Resultado da Consulta do Status do Serviço"""
    versao: Annotated[TVerConsStatServ, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    cStat: Annotated[TStat, Element] = None
    xMotivo: Annotated[TMotivo, Element] = None
    cUF: Annotated[TCodUfIBGE, Element] = None
    dhRecbto: Annotated[TDateTimeUTC, Element] = None
    tMed: Annotated[TMed, Element] = None
    dhRetorno: Annotated[TDateTimeUTC, Element] = None
    xObs: Annotated[TMotivo, Element] = None

