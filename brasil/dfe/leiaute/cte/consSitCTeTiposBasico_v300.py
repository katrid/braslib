# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: consSitCTeTiposBasico_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte

from .procCTe_v300 import *


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

    class _procEventoCTe(ComplexType):
        """Retornar procEventoCTe da versão correspondente do evento CT-e autorizado"""
        versao: Annotated[str, Attribute(enumeration=['1.04', '2.00', '3.00'])] = None

    procEventoCTe: Annotated[ElementList[_procEventoCTe], Element] = None


