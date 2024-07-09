# Generated by xsd2py.py
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposBasico_v103 import *


class TUfCons(str):
    """Tipo Sigla da UF consultada"""
    pass


class TVerConsCad(str):
    """Tipo Versão do Leiaute da Consulta Cadastro 2.00"""
    pass


class TConsCad(ComplexType):
    """Tipo Pedido de Consulta de cadastro de contribuintes"""
    versao: Annotated[TVerConsCad, Attribute] = None

    class _infCons(ComplexType):
        """Dados do Pedido de Consulta de cadastro de contribuintes"""
        xServ: Annotated[TServ, Element] = None
        UF: Annotated[TUfCons, Element] = None
        IE: Annotated[TIe, Element] = None
        CNPJ: Annotated[TCnpjVar, Element] = None
        CPF: Annotated[TCpfVar, Element] = None
        IE_CNPJ_CPF = Choice("IE", "CNPJ", "CPF")

    infCons: Annotated[_infCons, Element] = None


class TEndereco(ComplexType):
    """Tipo Dados do Endereço"""
    xLgr: Annotated[str, Element] = None
    nro: Annotated[str, Element] = None
    xCpl: Annotated[str, Element] = None
    xBairro: Annotated[str, Element] = None
    cMun: Annotated[TCodMunIBGE, Element] = None
    xMun: Annotated[str, Element] = None
    CEP: Annotated[str, Element] = None


class TRetConsCad(ComplexType):
    """Tipo Retorno Pedido de Consulta de cadastro de contribuintes"""
    versao: Annotated[TVerConsCad, Attribute] = None

    class _infCons(ComplexType):
        """Dados do Resultado doDados do Pedido de Consulta de cadastro de contribuintes"""
        verAplic: Annotated[TVerAplic, Element] = None
        cStat: Annotated[TStat, Element] = None
        xMotivo: Annotated[TMotivo, Element] = None
        UF: Annotated[TUfCons, Element] = None
        IE: Annotated[TIe, Element] = None
        CNPJ: Annotated[TCnpjVar, Element] = None
        CPF: Annotated[TCpfVar, Element] = None
        IE_CNPJ_CPF = Choice("IE", "CNPJ", "CPF")
        dhCons: Annotated[datetime, Element] = None
        cUF: Annotated[TCodUfIBGE, Element] = None

        class _infCad(ComplexType):
            """Informações cadastrais do contribuinte consultado"""
            IE: Annotated[TIe, Element] = None
            CNPJ: Annotated[TCnpjVar, Element] = None
            CPF: Annotated[TCpfVar, Element] = None
            CNPJ_CPF = Choice("CNPJ", "CPF")
            UF: Annotated[TUf, Element] = None
            cSit: Annotated[str, Element] = None
            indCredNFe: Annotated[str, Element] = None
            indCredCTe: Annotated[str, Element] = None
            xNome: Annotated[str, Element] = None
            xFant: Annotated[str, Element] = None
            xRegApur: Annotated[str, Element] = None
            CNAE: Annotated[str, Element] = None
            dIniAtiv: Annotated[xs:date, Element] = None
            dUltSit: Annotated[xs:date, Element] = None
            dBaixa: Annotated[xs:date, Element] = None
            IEUnica: Annotated[TIe, Element] = None
            IEAtual: Annotated[TIe, Element] = None
            ender: Annotated[TEndereco, Element] = None

        infCad: Annotated[List[_infCad], Element] = None

    infCons: Annotated[_infCons, Element] = None

