# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: e110112_v1.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe

from .tiposBasico_v103 import *


class detEvento(ComplexType):
    """Schema XML de validação do evento do cancelamento por substituição 110112"""
    versao: Annotated[str, Attribute(enumeration=['1.00'])] = None
    descEvento: Annotated[str, Element] = None
    cOrgaoAutor: Annotated[TCodUfIBGE, Element] = None
    tpAutor: Annotated[str, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    nProt: Annotated[TProt, Element] = None
    xJust: Annotated[TJust, Element] = None
    chNFeRef: Annotated[TChNFe, Element] = None


