# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: evPrestDesacordo_v4.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte

from .eventoCTeTiposBasico_v400 import *


class evPrestDesacordo(ComplexType):
    """Schema XML de validação do evento Prestação do Serviço em Desacordo 610110"""
    descEvento: Annotated[str, Element] = None
    indDesacordoOper: Annotated[str, Element] = None
    xObs: Annotated[str, Element] = None


