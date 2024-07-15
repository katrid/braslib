# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: cteModalDutoviario_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposGeralCTe_v300 import *
from .cteTiposBasico_v300 import *


class duto(ComplexType):
    """Informações do modal Dutoviário"""
    vTar: Annotated[TDec_0906Opc, Element] = None
    dIni: Annotated[TData, Element] = None
    dFim: Annotated[TData, Element] = None

