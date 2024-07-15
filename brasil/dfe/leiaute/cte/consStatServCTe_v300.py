# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: consStatServCTe_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .consStatServTiposBasico_v300 import *


class consStatServCte(TConsStatServ):
    """Schema XML de validação do Pedido de Consulta do Status do Serviço CT-e"""
    _xmlns = "http://www.portalfiscal.inf.br/cte"

