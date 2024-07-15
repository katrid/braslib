# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: enviNFe_v3.10.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .leiauteNFe_v310 import *


class enviNFe(TEnviNFe):
    """Schema XML de validação do Pedido de Concessão de Autorização da Nota Fiscal Eletrônica"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"

