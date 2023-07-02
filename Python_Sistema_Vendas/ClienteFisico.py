from Documento_CNPJ_CPF import Documento

class ClienteFisico:
    def __init__(self, nm_cliente, ds_cpf_cnpj_cliente):
        self.nm_cliente = nm_cliente
        self.ds_cpf_cnpj_cliente = Documento.cria_documento(ds_cpf_cnpj_cliente)
