# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: evEPECCTe_v4.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .eventoCTeTiposBasico_v400 import *


class evEPECCTe(ComplexType):
    """Schema XML de validação do evento de emissão prévia de emissão em contingência 
110113"""
    descEvento: Annotated[str, Element] = None
    xJust: Annotated[TJust, Element] = None
    vICMS: Annotated[TDec_1302, Element] = None
    vICMSST: Annotated[TDec_1302, Element] = None
    vTPrest: Annotated[TDec_1302, Element] = None
    vCarga: Annotated[TDec_1302, Element] = None

    class _toma4(ComplexType):
        """Indicador do \"papel\" do tomador do serviço no CT-e"""
        toma: Annotated[str, Element] = None
        UF: Annotated[TUf, Element] = None
        CNPJ: Annotated[TCnpjOpc, Element] = None
        CPF: Annotated[TCpf, Element] = None
        CNPJ_CPF = Choice("CNPJ", "CPF")
        IE: Annotated[TIeDest, Element] = None

    toma4: Annotated[_toma4, Element] = None
    modal: Annotated[TModTransp, Element] = None
    UFIni: Annotated[TUf, Element] = None
    UFFim: Annotated[TUf, Element] = None
    tpCTe: Annotated[str, Element] = None
    dhEmi: Annotated[TDateTimeUTC, Element] = None

