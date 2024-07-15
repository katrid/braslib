# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: e210210_v1.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import Annotated

from brasil.dfe.xsd import ComplexType, Attribute, Element


class detEvento(ComplexType):
    """Schema XML de validação do evento de Ciência da Operação"""
    versao: Annotated[str, Attribute(enumeration=['1.00'])] = None
    descEvento: Annotated[str, Element] = None


