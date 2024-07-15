# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: mdfeConsultaDFeTiposBasico_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/mdfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposGeralMDFe_v300 import *


class TVerMDFeConsultaDFe(str):
    """ Tipo Versão do Consulta DFe de MDF-e - 3.00"""
    pass


class TMDFeConsultaDFe(ComplexType):
    """Tipo Pedido de Consulta do Manifesto Eletrônico de Documentos Fiscais"""
    versao: Annotated[TVerMDFeConsultaDFe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    xServ: Annotated[TServ, Element] = None
    chMDFe: Annotated[TChNFe, Element] = None


class TMDFeDFe(ComplexType):
    """Tipo Documento Fiscal Eletrônico MDF-e"""

    class _procMDFe(ComplexType):
        """Autorização de Uso do MDF-e"""
        versao: Annotated[TVerMDFeConsultaDFe, Attribute] = None

    procMDFe: Annotated[_procMDFe, Element] = None

    class _procEventoMDFe(ComplexType):
        """Demais eventos vinculados ao MDF-e"""
        versao: Annotated[TVerMDFeConsultaDFe, Attribute] = None

    procEventoMDFe: Annotated[ElementList[_procEventoMDFe], Element] = None


class TRetMDFeConsultaDFe(ComplexType):
    """Tipo Retorno de Pedido de Consulta do Manifesto Eletrônico de Documentos Fiscais"""
    versao: Annotated[TVerMDFeConsultaDFe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    cStat: Annotated[TStat, Element] = None
    xMotivo: Annotated[TMotivo, Element] = None
    MDFeDFe: Annotated[TMDFeDFe, Element] = None

