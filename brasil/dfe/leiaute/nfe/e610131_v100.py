# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: e610131_v1.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposBasico_v103 import *


class detEvento(ComplexType):
    """Schema XML de validação do evento de Cancelamento do Comprovante de Entrega de CT-e"""
    versao: Annotated[str, Attribute(enumeration=['1.00'])] = None
    descEvento: Annotated[str, Element] = None
    cOrgaoAutor: Annotated[TCOrgaoIBGE, Element] = None
    tpAutor: Annotated[str, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    chCTe: Annotated[str, Element] = None
    nProtCTeCanc: Annotated[str, Element] = None

