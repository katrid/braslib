from __future__ import annotations
from datetime import date, datetime
from decimal import Decimal
from typing import List
from brasil.dfe.xsd import SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime
from .leiauteConsStatServ_v400 import *


class consStatServ(TConsStatServ):
    _xmlns = 'http://www.portalfiscal.inf.br/nfe'

