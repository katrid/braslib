# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: consSitCTeTiposBasico_v4.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposGeralCTe_v400 import *
from .procCTe_v400 import *


class TVerConsSitCTe(str):
    """ Tipo Versão do Consulta situação de CT-e - 4.00"""
    pass


class TConsSitCTe(ComplexType):
    """Tipo Pedido de Consulta da Situação Atual do Conhecimento de Transporte eletrônico"""
    versao: Annotated[TVerConsSitCTe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    xServ: Annotated[TServ, Element] = None
    chCTe: Annotated[TChDFe, Element] = None


class TRetConsSitCTe(ComplexType):
    """Tipo Retorno de Pedido de Consulta da Situação Atual do Conhecimento de Transporte eletrônico"""
    versao: Annotated[TVerConsSitCTe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    cStat: Annotated[TStat, Element] = None
    xMotivo: Annotated[TMotivo, Element] = None
    cUF: Annotated[TCodUfIBGE, Element] = None
    protCTe: Annotated[TProtCTe, Element] = None

    class _procEventoCTe(ComplexType):
        """Retornar procEventoCTe da versão correspondente do evento CT-e autorizado"""
        versao: Annotated[str, Attribute(enumeration=['1.04', '2.00', '3.00', '4.00'])] = None

    procEventoCTe: Annotated[ElementList[_procEventoCTe], Element] = None

