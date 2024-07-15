# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: e411500_v1.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposBasico_v103 import *


class TRespPedido(ComplexType):
    """Resposta a um tpEvento 111500 ou 111501 """
    statPrazo: Annotated[str, Element] = None

    class _itemPedido(ComplexType):
        """Item do Pedido de Prorrogação"""
        numItem: Annotated[str, Attribute(pattern=r'[0-9]{1,3}')] = None
        statPedido: Annotated[str, Element] = None
        justStatus: Annotated[str, Element] = None
        justStaOutra: Annotated[str, Element] = None

    itemPedido: Annotated[ElementList[_itemPedido], Element] = None


class detEvento(ComplexType):
    """Informações do Fisco"""
    versao: Annotated[str, Attribute(enumeration=['1.00'])] = None
    descEvento: Annotated[str, Element] = None
    idPedido: Annotated[str, Element] = None
    respPedido: Annotated[TRespPedido, Element] = None

