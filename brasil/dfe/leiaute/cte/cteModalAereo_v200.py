# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: cteModalAereo_v2.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposGeralCTe_v200 import *


class aereo(ComplexType):
    """Informações do modal Aéreo"""
    nMinu: Annotated[str, Element] = None
    nOCA: Annotated[str, Element] = None
    dPrevAereo: Annotated[TData, Element] = None
    xLAgEmi: Annotated[str, Element] = None
    IdT: Annotated[str, Element] = None

    class _tarifa(ComplexType):
        """Informações de tarifa"""
        CL: Annotated[str, Element] = None
        cTar: Annotated[str, Element] = None
        vTar: Annotated[TDec_1302, Element] = None

    tarifa: Annotated[_tarifa, Element] = None

    class _natCarga(ComplexType):
        """Natureza da carga"""
        xDime: Annotated[str, Element] = None
        cInfManu: Annotated[ElementList[str], Element] = None
        cIMP: Annotated[ElementList[str], Element] = None

    natCarga: Annotated[_natCarga, Element] = None

