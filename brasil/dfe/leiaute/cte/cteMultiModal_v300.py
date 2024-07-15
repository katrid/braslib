# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: cteMultiModal_v3.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposGeralCTe_v300 import *
from .cteTiposBasico_v300 import *


class multimodal(ComplexType):
    """Informações do Multimodal"""
    COTM: Annotated[str, Element] = None
    indNegociavel: Annotated[str, Element] = None

    class _seg(ComplexType):
        """Informações de Seguro do Multimodal"""

        class _infSeg(ComplexType):
            """Informações da seguradora"""
            xSeg: Annotated[str, Element] = None
            CNPJ: Annotated[TCnpjOpc, Element] = None

        infSeg: Annotated[_infSeg, Element] = None
        nApol: Annotated[str, Element] = None
        nAver: Annotated[str, Element] = None

    seg: Annotated[_seg, Element] = None

