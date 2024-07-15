# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: eventoEPEC_v0.01.xsd
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature
from .tiposBasico_v310 import *


class TVerEvento(str):
    """Versão do Tipo do Evento"""
    pass


class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 91 RFB)"""
    pass


class envEvento(ComplexType):
    versao: Annotated[TVerEvento, Attribute] = None
    idLote: Annotated[str, Element] = None

    class _evento(ComplexType):
        """Evento, um lote pode conter até 20 eventos"""
        versao: Annotated[TVerEvento, Attribute] = None

        class _infEvento(ComplexType):
            """Grupo de informações do registro do Evento"""
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
            verEvento: Annotated[TVerEvento, Element] = None

            class _detEvento(ComplexType):
                """Informações de detalhes do evento"""
                versao: Annotated[TVerEvento, Attribute] = None
                descEvento: Annotated[str, Element] = None
                cOrgaoAutor: Annotated[TCodUfIBGE, Element] = None
                tpAutor: Annotated[str, Element] = None
                verAplic: Annotated[TVerAplic, Element] = None
                dhEmi: Annotated[TDateTimeUTC, Element] = None
                tpNF: Annotated[str, Element] = None
                IE: Annotated[TIe, Element] = None

                class _dest(ComplexType):
                    UF: Annotated[TUf, Element] = None
                    CNPJ: Annotated[TCnpjOpc, Element] = None
                    CPF: Annotated[TCpf, Element] = None
                    idEstrangeiro: Annotated[str, Element] = None
                    CNPJ_CPF_idEstrangeiro = Choice("CNPJ", "CPF", "idEstrangeiro")

                dest: Annotated[_dest, Element] = None
                vNF: Annotated[TDec_1302, Element] = None
                vICMS: Annotated[TDec_1302, Element] = None

            detEvento: Annotated[_detEvento, Element] = None

        infEvento: Annotated[_infEvento, Element] = None
        Signature: Annotated[XmlSignature, Element] = None

    evento: Annotated[ElementList[_evento], Element] = None

