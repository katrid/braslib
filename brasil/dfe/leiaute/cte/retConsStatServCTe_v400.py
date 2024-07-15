# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: retConsStatServCTe_v4.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .consStatServTiposBasico_v400 import *


class retConsStatServCTe(TRetConsStatServ):
    """Schema XML de validação do Resultado da Consulta do Status do Serviço de CT-e"""
    _xmlns = "http://www.portalfiscal.inf.br/cte"

