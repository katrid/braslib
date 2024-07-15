# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: retDistDFeInt_v1.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposDistDFe_v100 import *


class retDistDFeInt(ComplexType):
    """Schema do resultado do pedido de distribuição de DF-e de interesse"""
    versao: Annotated[TVerDistDFe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    cStat: Annotated[TStat, Element] = None
    xMotivo: Annotated[TMotivo, Element] = None
    dhResp: Annotated[str, Element] = None
    ultNSU: Annotated[TNSU, Element] = None
    maxNSU: Annotated[TNSU, Element] = None

    class _loteDistDFeInt(ComplexType):
        """Conjunto de informações resumidas e documentos fiscais eletrônicos de interesse da pessoa ou empresa. """

        class _docZip(ComplexType):
            value: base64Binary = None
            """Informação resumida ou documento fiscal eletrônico de interesse da pessoa ou empresa. O conteúdo desta tag estará compactado no padrão gZip. O tipo do campo é base64Binary."""

        docZip: Annotated[ElementList[_docZip], Element] = None

    loteDistDFeInt: Annotated[_loteDistDFeInt, Element] = None

