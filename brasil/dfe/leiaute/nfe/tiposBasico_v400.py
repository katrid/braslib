# Generated by xsd2py.py
# xmlns: http://www.portalfiscal.inf.br/nfe
from typing import List, Annotated
from datetime import date, datetime
from decimal import Decimal

from brasil.dfe.xsd import Choice, SimpleType, ComplexType, Attribute, Element, TString, Restriction, ID, base64Binary, anyURI, string, dateTime, TXML, ElementList, XmlSignature


class TCodUfIBGE(str):
    """Tipo Código da UF da tabela do IBGE"""
    pass


class TCodMunIBGE(str):
    """Tipo Código do Município da tabela do IBGE"""
    pass


class TChNFe(str):
    """Tipo Chave da Nota Fiscal Eletrônica"""
    pass


class TProt(str):
    """Tipo Número do Protocolo de Status"""
    pass


class TRec(str):
    """Tipo Número do Recibo do envio de lote de NF-e"""
    pass


class TStat(str):
    """Tipo Código da Mensagem enviada"""
    pass


class TCnpj(str):
    """Tipo Número do CNPJ"""
    pass


class TCnpjVar(str):
    """Tipo Número do CNPJ tmanho varíavel (3-14)"""
    pass


class TCnpjOpc(str):
    """Tipo Número do CNPJ Opcional"""
    pass


class TCpf(str):
    """Tipo Número do CPF"""
    pass


class TCpfVar(str):
    """Tipo Número do CPF de tamanho variável (3-11)"""
    pass


class TDec_0104v(Decimal):
    """Tipo Decimal com até 1 dígitos inteiros, podendo ter de 1 até 4 decimais"""
    _xs_dec = (1, 4)
    _xs_optional = False


class TDec_0204v(Decimal):
    """Tipo Decimal com até 2 dígitos inteiros, podendo ter de 1 até 4 decimais"""
    _xs_dec = (2, 4)
    _xs_optional = False


class TDec_0302a04(Decimal):
    """Tipo Decimal com até 3 dígitos inteiros, podendo ter de 2 até 4 decimais"""
    _xs_dec = (3, 2)
    _xs_optional = False


class TDec_0302a04Opc(Decimal):
    """Tipo Decimal com até 3 dígitos inteiros e 2 até 4 decimais. Utilizados em TAGs opcionais, não aceita valor zero."""
    _xs_dec = (3, 2)
    _xs_optional = True


class TDec_0302Max100(Decimal):
    """Tipo Decimal com 3 inteiros (no máximo 100), com 2 decimais"""
    _xs_dec = (3, 2)
    _xs_optional = False


class TDec_0304Max100(Decimal):
    """Tipo Decimal com 3 inteiros (no máximo 100), com 4 decimais"""
    _xs_dec = (3, 4)
    _xs_optional = False


class TDec_0302a04Max100(Decimal):
    """Tipo Decimal com 3 inteiros (no máximo 100), com até 4 decimais"""
    _xs_dec = (3, 2)
    _xs_optional = False


class TDec_0803v(Decimal):
    """Tipo Decimal com 8 inteiros, podendo ter de 1 até 3 decimais"""
    _xs_dec = (8, 3)
    _xs_optional = False


class TDec_1104(Decimal):
    """Tipo Decimal com 11 inteiros, podendo ter 4 decimais"""
    _xs_dec = (11, 4)
    _xs_optional = False


class TDec_1104v(Decimal):
    """Tipo Decimal com 11 inteiros, podendo ter de 1 até 4 decimais"""
    _xs_dec = (11, 4)
    _xs_optional = False


class TDec_1104Opc(Decimal):
    """Tipo Decimal com 11 inteiros, podendo ter 4 decimais (utilizado em tags opcionais)"""
    _xs_dec = (11, 4)
    _xs_optional = True


class TDec_1110v(Decimal):
    """Tipo Decimal com 11 inteiros, podendo ter de 1 até 10 decimais"""
    _xs_dec = (11, 10)
    _xs_optional = False


class TDec_1203(Decimal):
    """Tipo Decimal com 12 inteiros, podendo ter  3 decimais"""
    _xs_dec = (12, 3)
    _xs_optional = False


class TDec_1204(Decimal):
    """Tipo Decimal com 12 inteiros e 4 decimais"""
    _xs_dec = (12, 4)
    _xs_optional = False


class TDec_1204v(Decimal):
    """Tipo Decimal com 12 inteiros de 1 até 4 decimais"""
    _xs_dec = (12, 4)
    _xs_optional = False


class TDec_1204Opc(Decimal):
    """Tipo Decimal com 12 inteiros com 1 até 4 decimais"""
    _xs_dec = (12, 4)
    _xs_optional = True


class TDec_1204temperatura(Decimal):
    """Tipo Decimal com 12 inteiros, 1 a 4 decimais"""
    _xs_dec = (12, 4)
    _xs_optional = False


class TDec_1302(Decimal):
    """Tipo Decimal com 15 dígitos, sendo 13 de corpo e 2 decimais"""
    _xs_dec = (13, 2)
    _xs_optional = False


class TDec_1302Opc(Decimal):
    """Tipo Decimal com 15 dígitos, sendo 13 de corpo e 2 decimais, utilizado em tags opcionais"""
    _xs_dec = (13, 2)
    _xs_optional = True


class TIeDest(str):
    """Tipo Inscrição Estadual do Destinatário // alterado para aceitar vazio ou ISENTO - maio/2010 v2.0"""
    pass


class TIeDestNaoIsento(str):
    """Tipo Inscrição Estadual do Destinatário // alterado para aceitar vazio ou ISENTO - maio/2010 v2.0"""
    pass


class TIeST(str):
    """Tipo Inscrição Estadual do ST // acrescentado EM 24/10/08"""
    pass


class TIe(str):
    """Tipo Inscrição Estadual do Emitente // alterado EM 24/10/08 para aceitar ISENTO"""
    pass


class TMod(str):
    """Tipo Modelo Documento Fiscal"""
    pass


class TNF(str):
    """Tipo Número do Documento Fiscal"""
    pass


class TSerie(str):
    """Tipo Série do Documento Fiscal """
    pass


class TUf(str):
    """Tipo Sigla da UF"""
    pass


class TUfEmi(str):
    """Tipo Sigla da UF de emissor // acrescentado em 24/10/08 """
    pass


class TAmb(str):
    """Tipo Ambiente"""
    pass


class TVerAplic(TString):
    """Tipo Versão do Aplicativo"""
    pass


class TMotivo(TString):
    """Tipo Motivo"""
    pass


class TJust(TString):
    """Tipo Justificativa"""
    pass


class TServ(TString):
    """Tipo Serviço solicitado"""
    pass


class Tano(str):
    """ Tipo ano"""
    pass


class TMed(str):
    """ Tipo temp médio em segundos"""
    pass


class TString(str):
    """ Tipo string genérico"""
    pass


class TData(str):
    """ Tipo data AAAA-MM-DD"""
    pass


class TTime(str):
    """ Tipo hora HH:MM:SS // tipo acrescentado na v2.0"""
    pass


class TDateTimeUTC(str):
    """Data e Hora, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)"""
    pass


class TPlaca(str):
    pass


class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 90 RFB)"""
    pass

