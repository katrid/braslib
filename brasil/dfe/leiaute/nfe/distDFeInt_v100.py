# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: distDFeInt_v1.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposDistDFe_v100 import *


class distDFeInt(ComplexType):
    """Schema de pedido de distribuição de DF-e de interesse"""
    versao: Annotated[TVerDistDFe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    cUFAutor: Annotated[TCodUfIBGE, Element] = None
    CNPJ: Annotated[TCnpj, Element] = None
    CPF: Annotated[TCpf, Element] = None
    CNPJ_CPF = Choice("CNPJ", "CPF")

    class _distNSU(ComplexType):
        """Grupo para distribuir DF-e de interesse"""
        ultNSU: Annotated[TNSU, Element] = None

    distNSU: Annotated[_distNSU, Element] = None

    class _consNSU(ComplexType):
        """Grupo para consultar um DF-e a partir de um NSU específico"""
        NSU: Annotated[TNSU, Element] = None

    consNSU: Annotated[_consNSU, Element] = None
    distNSU_consNSU = Choice("distNSU", "consNSU")

