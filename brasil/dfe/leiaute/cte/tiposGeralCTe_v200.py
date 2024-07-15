# Generated by xsd2py.py
# DO NOT CHANGE THIS FILE (use compile override instead)
# xsd: tiposGeralCTe_v2.00.xsd
# xmlns: http://www.portalfiscal.inf.br/cte
from decimal import Decimal


class TAmb(str):
    """Tipo Ambiente"""
    pass


class Tano(str):
    """ Tipo ano"""
    pass


class TCodUfIBGE(str):
    """Tipo Código da UF da tabela do IBGE"""
    pass


class TCodMunIBGE(str):
    """Tipo Código do Município da tabela do IBGE"""
    pass


class TCOrgaoIBGE(str):
    """Tipo Código de orgão (UF da tabela do IBGE + 90 SUFRAMA)"""
    pass


class TChNFe(str):
    """Tipo Chave da Nota Fiscal Eletrônica"""
    pass


class TCnpj(str):
    """Tipo Número do CNPJ"""
    pass


class TFone(str):
    """Tipo Número do Telefone"""
    pass


class TCnpjVar(str):
    """Tipo Número do CNPJ tamanho varíavel (3-14)"""
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


class TData(str):
    """ Tipo data AAAA-MM-DD"""
    pass


class TDec_0302(Decimal):
    """Tipo Decimal com 5 dígitos, sendo 3 de corpo e 2 decimais"""
    _xs_dec = (3, 2)
    _xs_optional = False


class TDec_0303(Decimal):
    """Tipo Decimal com 6 dígitos, sendo 3 de corpo e 3 decimais"""
    _xs_dec = (3, 3)
    _xs_optional = False


class TDec_0302_0303(Decimal):
    """Tipo Decimal com 6  ou 5 dígitos, sendo 3 de corpo e 3 ou 2 decimais"""
    _xs_dec = (3, 2)
    _xs_optional = False


class TDec_0302Opc(Decimal):
    """Tipo Decimal com 5 dígitos, sendo 3 de corpo e 2 decimais, utilizado em tags opcionais"""
    _xs_dec = (3, 2)
    _xs_optional = True


class TDec_0803(Decimal):
    """Tipo Decimal com 11 dígitos, sendo 8 de corpo e 3 decimais"""
    _xs_dec = (8, 3)
    _xs_optional = False


class TDec_0803Opc(Decimal):
    """Tipo Decimal com 11 dígitos, sendo 8 de corpo e 3 decimais utilizado em tags opcionais"""
    _xs_dec = (8, 3)
    _xs_optional = True


class TDec_0804(Decimal):
    """Tipo Decimal com 12 dígitos, sendo 8 de corpo e 4decimais"""
    _xs_dec = (8, 4)
    _xs_optional = False


class TDec_0804Opc(Decimal):
    """Tipo Decimal com 12 dígitos, sendo 8 de corpo e 4 decimais, utilizado em tags opcionais"""
    _xs_dec = (8, 4)
    _xs_optional = True


class TDec_0906Opc(Decimal):
    """Tipo Decimal com 15 dígitos, sendo 9 de corpo e 6 decimais, utilizado em tags opcionais"""
    _xs_dec = (9, 6)
    _xs_optional = True


class TDec_1104(Decimal):
    """Tipo Decimal com 15 dígitos, sendo 11 de corpo e 4 decimais"""
    _xs_dec = (11, 4)
    _xs_optional = False


class TDec_1104Opc(Decimal):
    """Tipo Decimal com 15 dígitos, sendo 11 de corpo e 4 decimais, utilizado em tags opcionais"""
    _xs_dec = (11, 4)
    _xs_optional = True


class TDec_1203(Decimal):
    """Tipo Decimal com 15 dígitos, sendo 12 de corpo e 3 decimais"""
    _xs_dec = (12, 3)
    _xs_optional = False


class TDec_1203Opc(Decimal):
    """Tipo Decimal com 15 dígitos, sendo 12 de corpo e 3 decimais, utilizado em tags opcionais"""
    _xs_dec = (12, 3)
    _xs_optional = True


class TDec_1204(Decimal):
    """Tipo Decimal com 16 dígitos, sendo 12 de corpo e 4 decimais"""
    _xs_dec = (12, 4)
    _xs_optional = False


class TDec_1204Opc(Decimal):
    """Tipo Decimal com 16 dígitos, sendo 12 de corpo e 4 decimais, utilizado em tags opcionais"""
    _xs_dec = (12, 4)
    _xs_optional = True


class TDec_1302(Decimal):
    """Tipo Decimal com 15 dígitos, sendo 13 de corpo e 2 decimais"""
    _xs_dec = (13, 2)
    _xs_optional = False


class TDec_1302Opc(Decimal):
    """Tipo Decimal com 15 dígitos, sendo 13 de corpo e 2 decimais, utilizado em tags opcionais"""
    _xs_dec = (13, 2)
    _xs_optional = True


class TIe(str):
    """Tipo Inscrição Estadual do Emitente"""
    pass


class TIeDest(str):
    """Tipo Inscrição Estadual do Destinatário"""
    pass


class TString(str):
    """ Tipo string genérico"""
    pass


class TJust(str):
    """Tipo Justificativa"""
    pass


class TMed(str):
    """ Tipo temp médio em segundos"""
    pass


class TModCT(str):
    """Tipo Modelo Documento Fiscal"""
    pass


class TModNF(str):
    """Tipo Modelo Documento Fiscal - NF Remetente"""
    pass


class TtipoUnidTransp(str):
    """Tipo da Unidade de Transporte"""
    pass


class TtipoUnidCarga(str):
    """Tipo da Unidade de Carga"""
    pass


class TMotivo(str):
    """Tipo Motivo"""
    pass


class TNF(str):
    """Tipo Número do Documento Fiscal"""
    pass


class TProt(str):
    """Tipo Número do Protocolo de Status"""
    pass


class TRec(str):
    """Tipo Número do Recibo do envio de lote de NF-e"""
    pass


class TSerie(str):
    """Tipo Série do Documento Fiscal """
    pass


class TServ(str):
    """Tipo Serviço solicitado"""
    pass


class TStat(str):
    """Tipo Código da Mensagem enviada"""
    pass


class TUf(str):
    """Tipo Sigla da UF"""
    pass


class TUF_sem_EX(str):
    """Tipo Sigla da UF, sem Exterior"""
    pass


class TVerAplic(str):
    """Tipo Versão do Aplicativo"""
    pass


class TLatitude(str):
    """Coordenada geográfica Latitude"""
    pass


class TLongitude(str):
    """Coordenada geográfica Longitude"""
    pass


