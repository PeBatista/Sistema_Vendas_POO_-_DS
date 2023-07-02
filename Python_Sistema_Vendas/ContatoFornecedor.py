from Telefone import TelefonesBr

class ContatoFornecedor:
    def __init__(self, cd_contato_fornecedor, cd_fornecedor, ds_telefone_fornecedor, ds_cel_fornecedor, ds_endereco_moradia_empresa):
        self.cd_contato_fornecedor = cd_contato_fornecedor
        self.cd_fornecedor = cd_fornecedor
        self.ds_telefone_fornecedor = TelefonesBr(ds_telefone_fornecedor)
        self.ds_cel_fornecedor = TelefonesBr(ds_cel_fornecedor)
        self.ds_endereco_moradia_empresa = ds_endereco_moradia_empresa
