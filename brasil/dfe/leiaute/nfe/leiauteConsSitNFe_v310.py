# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: leiauteConsSitNFe_v3.10.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe

from .tiposBasico_v310 import *


class TVerConsSitNFe(str):
    """Tipo Versão do Leiaute da Cosulta situação NF-e - 3.10"""
    pass


class TConsSitNFe(ComplexType):
    """Tipo Pedido de Consulta da Situação Atual da Nota Fiscal Eletrônica"""
    versao: Annotated[TVerConsSitNFe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    xServ: Annotated[TServ, Element] = None
    chNFe: Annotated[TChNFe, Element] = None


class TVerNFe(str):
    """ Tipo Versão da NF-e"""
    pass


class TProtNFe(ComplexType):
    """Tipo Protocolo de status resultado do processamento da NF-e"""
    versao: Annotated[TVerNFe, Attribute] = None

    class _infProt(ComplexType):
        """Dados do protocolo de status"""
        Id: Annotated[str, Attribute] = None
        tpAmb: Annotated[TAmb, Element] = None
        verAplic: Annotated[TVerAplic, Element] = None
        chNFe: Annotated[TChNFe, Element] = None
        dhRecbto: Annotated[datetime, Element] = None
        nProt: Annotated[TProt, Element] = None
        digVal: Annotated[TXML, Element] = None
        cStat: Annotated[TStat, Element] = None
        xMotivo: Annotated[TMotivo, Element] = None

    infProt: Annotated[_infProt, Element] = None
    Signature: Annotated[XmlSignature, Element] = None


class TVerCancNFe(str):
    """Tipo Versão do leiaute de Cancelamento de NF-e - 2.00/1.07"""
    pass


class TRetCancNFe(ComplexType):
    """Tipo retorno Pedido de Cancelamento da Nota Fiscal Eletrônica"""
    versao: Annotated[TVerCancNFe, Attribute] = None

    class _infCanc(ComplexType):
        """Dados do Resultado do Pedido de Cancelamento da Nota Fiscal Eletrônica"""
        Id: Annotated[str, Attribute] = None
        tpAmb: Annotated[TAmb, Element] = None
        verAplic: Annotated[TVerAplic, Element] = None
        cStat: Annotated[TStat, Element] = None
        xMotivo: Annotated[TMotivo, Element] = None
        cUF: Annotated[TCodUfIBGE, Element] = None
        chNFe: Annotated[TChNFe, Element] = None
        dhRecbto: Annotated[datetime, Element] = None
        nProt: Annotated[TProt, Element] = None

    infCanc: Annotated[_infCanc, Element] = None
    Signature: Annotated[XmlSignature, Element] = None


class TRetVerEvento(str):
    """Tipo Versão do Evento"""
    pass


class TRetEvento(ComplexType):
    """Tipo retorno do Evento"""
    versao: Annotated[TRetVerEvento, Attribute] = None

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
        CNPJDest: Annotated[TCnpjOpc, Element] = None
        CPFDest: Annotated[TCpf, Element] = None
        CNPJDest_CPFDest = Choice("CNPJDest", "CPFDest")
        emailDest: Annotated[str, Element] = None
        dhRegEvento: Annotated[TDateTimeUTC, Element] = None
        nProt: Annotated[TProt, Element] = None

    infEvento: Annotated[_infEvento, Element] = None
    Signature: Annotated[XmlSignature, Element] = None


class TVerEvento(str):
    """Tipo Versão do Evento 1.00"""
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
            """Detalhe Específico do Evento"""

        detEvento: Annotated[_detEvento, Element] = None

    infEvento: Annotated[_infEvento, Element] = None
    Signature: Annotated[XmlSignature, Element] = None


class TProcEvento(ComplexType):
    """Tipo procEvento"""
    versao: Annotated[TVerEvento, Attribute] = None
    evento: Annotated[TEvento, Element] = None
    retEvento: Annotated[TRetEvento, Element] = None


class TRetConsSitNFe(ComplexType):
    """Tipo Retorno de Pedido de Consulta da Situação Atual da Nota Fiscal Eletrônica """
    versao: Annotated[TVerConsSitNFe, Attribute] = None
    tpAmb: Annotated[TAmb, Element] = None
    verAplic: Annotated[TVerAplic, Element] = None
    cStat: Annotated[TStat, Element] = None
    xMotivo: Annotated[TMotivo, Element] = None
    cUF: Annotated[TCodUfIBGE, Element] = None
    dhRecbto: Annotated[TDateTimeUTC, Element] = None
    chNFe: Annotated[TChNFe, Element] = None
    protNFe: Annotated[TProtNFe, Element] = None
    retCancNFe: Annotated[TRetCancNFe, Element] = None
    procEventoNFe: Annotated[ElementList[TProcEvento], Element] = None


