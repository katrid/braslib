# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: consSitCTeTiposBasico_v2.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte

from .cancCTeTiposBasico_v200 import *
from .consReciCTeTiposBasico_v200 import *
from .eventoCTeTiposBasico_v200 import *


class TVerConsSitCTe(str):
    """ Tipo Versão do Consulta situação de CT-e - 2.00"""
    pass


class TConsSitCTe(ComplexType):
    """Tipo Pedido de Consulta da Situação Atual do Conhecimento de Transporte eletrônico"""
    versao: Annotated[TVerConsSitCTe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    xServ: Annotated[TServ, Element] = None
    chCTe: Annotated[TChNFe, Element] = None


class TRetConsSitCTe(ComplexType):
    """Tipo Retorno de Pedido de Consulta da Situação Atual do Conhecimento de Transporte eletrônico"""
    versao: Annotated[TVerConsSitCTe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    cStat: Annotated[TStat, Element] = None
    xMotivo: Annotated[TMotivo, Element] = None
    cUF: Annotated[TCodUfIBGE, Element] = None
    protCTe: Annotated[TProtCTe, Element] = None
    retCancCTe: Annotated[TRetCancCTe, Element] = None
    protCTe_retCancCTe = Choice("protCTe", "retCancCTe")
    procEventoCTe: Annotated[ElementList[TProcEvento], Element] = None


