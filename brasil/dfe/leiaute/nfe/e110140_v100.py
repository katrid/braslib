# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: e110140_v1.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe

from .tiposBasico_v103 import *


class detEvento(ComplexType):
    versao: Annotated[str, Attribute(enumeration=['1.00'])] = None
    descEvento: Annotated[str, Element] = None
    cOrgaoAutor: Annotated[str, Element] = None
    tpAutor: Annotated[str, Element] = None
    verAplic: Annotated[str, Element] = None
    dhEmi: Annotated[str, Element] = None
    tpNF: Annotated[str, Element] = None
    IE: Annotated[str, Element] = None

    class _dest(ComplexType):
        UF: Annotated[str, Element] = None
        CNPJ: Annotated[TCnpj, Element] = None
        CPF: Annotated[TCpf, Element] = None
        idEstrangeiro: Annotated[str, Element] = None
        CNPJ_CPF_idEstrangeiro = Choice("CNPJ", "CPF", "idEstrangeiro")
        IE: Annotated[str, Element] = None
        vNF: Annotated[str, Element] = None
        vICMS: Annotated[str, Element] = None
        vST: Annotated[str, Element] = None

    dest: Annotated[_dest, Element] = None

descEvento: Annotated[str, Element] = None
tpAutor: Annotated[str, Element] = None

class verAplic(TVerAplic):
    """Versão do Aplicativo do Autor do Evento"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"


class dhEmi(TDateTimeUTC):
    """Data de emissão no formato UTC.  AAAA-MM-DDThh:mm:ssTZD"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"

tpNF: Annotated[str, Element] = None

class cOrgaoAutor(TCodUfIBGE):
    _xmlns = "http://www.portalfiscal.inf.br/nfe"

IE: Annotated[str, Element] = None

class UF(TUf):
    """Sigla UF do destinatário. Informar \"EX\" no caso de operação com o exterior"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"


class vNF(TDec_1302):
    """Valor total da NF-e"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"


class vICMS(TDec_1302):
    """Valor total do ICMS"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"


class vST(TDec_1302):
    """Valor total do ICMS de Substituição Tributária"""
    _xmlns = "http://www.portalfiscal.inf.br/nfe"


