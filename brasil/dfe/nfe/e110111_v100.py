from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .tiposBasico_v103 import *


class detEvento(ComplexType):
    descEvento: str = Element(str)
    nProt: TProt = Element(TProt)
    xJust: TJust = Element(TJust)
    versao: str = Attribute(None)

detEvento: detEvento
