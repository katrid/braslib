# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: leiauteEvento_v1.00.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe

from .tiposBasico_v103 import *


class TVerEvento(str):
    """Tipo Versão do Evento"""
    pass


class TEvento(ComplexType):
    """Tipo Evento"""
    versao: Annotated[TVerEvento, Attribute] = None

    class _infEvento(ComplexType):
        Id: Annotated[str, Attribute(pattern=r'ID[0-9]{52}')] = None
        cOrgao: Annotated[TCOrgaoIBGE, Element] = None
        tpAmb: Annotated[TAmb, Element] = None
        CNPJ: Annotated[TCnpjOpc, Element] = None
        CPF: Annotated[TCpf, Element] = None
        CNPJ_CPF = Choice("CNPJ", "CPF")
        chNFe: Annotated[TChNFe, Element] = None
        dhEvento: Annotated[TDateTimeUTC, Element] = None
        tpEvento: Annotated[str, Element] = None
        nSeqEvento: Annotated[str, Element] = None
        verEvento: Annotated[str, Element] = None

        class _detEvento(ComplexType):
            """informações específicas do evento"""

        detEvento: Annotated[_detEvento, Element] = None

    infEvento: Annotated[_infEvento, Element] = None
    Signature: Annotated[XmlSignature, Element] = None


class TRetEvento(ComplexType):
    """Tipo retorno do Evento"""
    versao: Annotated[TVerEvento, Attribute] = None

    class _infEvento(ComplexType):
        Id: Annotated[str, Attribute(pattern=r'ID[0-9]{15}')] = None
        tpAmb: Annotated[TAmb, Element] = None
        verAplic: Annotated[TVerAplic, Element] = None
        cOrgao: Annotated[TCOrgaoIBGE, Element] = None
        cStat: Annotated[TStat, Element] = None
        xMotivo: Annotated[TMotivo, Element] = None
        chNFe: Annotated[TChNFe, Element] = None
        tpEvento: Annotated[str, Element] = None
        xEvento: Annotated[str, Element] = None
        nSeqEvento: Annotated[str, Element] = None
        cOrgaoAutor: Annotated[TCOrgaoIBGE, Element] = None
        CNPJDest: Annotated[TCnpjOpc, Element] = None
        CPFDest: Annotated[TCpf, Element] = None
        CNPJDest_CPFDest = Choice("CNPJDest", "CPFDest")
        emailDest: Annotated[str, Element] = None
        dhRegEvento: Annotated[str, Element] = None
        nProt: Annotated[TProt, Element] = None

    infEvento: Annotated[_infEvento, Element] = None
    Signature: Annotated[XmlSignature, Element] = None


class TVerEnvEvento(str):
    """Tipo Versão do EnvEvento"""
    pass


class TEnvEvento(ComplexType):
    """ Tipo Lote de Envio"""
    versao: Annotated[TVerEnvEvento, Attribute] = None
    idLote: Annotated[str, Element] = None
    evento: Annotated[ElementList[TEvento], Element] = None


class TRetEnvEvento(ComplexType):
    """ Tipo Retorno de Lote de Envio"""
    versao: Annotated[TVerEnvEvento, Attribute] = None
    idLote: Annotated[str, Element] = None
    tpAmb: Annotated[TAmb, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    cOrgao: Annotated[TCOrgaoIBGE, Element] = None
    cStat: Annotated[TStat, Element] = None
    xMotivo: Annotated[TMotivo, Element] = None
    retEvento: Annotated[ElementList[TRetEvento], Element] = None


class TProcEvento(ComplexType):
    """Tipo procEvento"""
    versao: Annotated[TVerEvento, Attribute] = None
    evento: Annotated[TEvento, Element] = None
    retEvento: Annotated[TRetEvento, Element] = None


