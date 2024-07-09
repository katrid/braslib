# Generated by xsd2py.py
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .leiauteInutNFe_v400 import *


class inutNFe(TInutNFe):
    """Schema XML de validação do Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"

