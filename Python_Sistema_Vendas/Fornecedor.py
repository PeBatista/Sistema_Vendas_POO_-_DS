from Documento_CNPJ_CPF import Documento

class Fornecedor:
    def __init__(self, nm_fornecedor, ds_cpf_fornecedor, ds_rg_fornecedor, sg_genero_fornecedor):
        self.nm_fornecedor = nm_fornecedor
        self.ds_cpf_fornecedor = Documento.cria_documento(ds_cpf_fornecedor)
        self.ds_rg_fornecedor = ds_rg_fornecedor
        self.sg_genero_fornecedor = sg_genero_fornecedor
    
        
        