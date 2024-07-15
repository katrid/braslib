# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: mdfeModalFerroviario_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/mdfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposGeralMDFe_v300 import *


class ferrov(ComplexType):
    """Informações do modal Ferroviário"""

    class _trem(ComplexType):
        """Informações da composição do trem"""
        xPref: Annotated[str, Element] = None
        dhTrem: Annotated[TDateTimeUTC, Element] = None
        xOri: Annotated[str, Element] = None
        xDest: Annotated[str, Element] = None
        qVag: Annotated[str, Element] = None

    trem: Annotated[_trem, Element] = None

    class _vag(ComplexType):
        """informações dos Vagões"""
        pesoBC: Annotated[TDec_0303, Element] = None
        pesoR: Annotated[TDec_0303, Element] = None
        tpVag: Annotated[str, Element] = None
        serie: Annotated[str, Element] = None
        nVag: Annotated[str, Element] = None
        nSeq: Annotated[str, Element] = None
        TU: Annotated[TDec_0302_0303, Element] = None

    vag: Annotated[ElementList[_vag], Element] = None

