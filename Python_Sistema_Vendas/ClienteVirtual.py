from Documento_CNPJ_CPF import Documento

class ClienteVirtual:
    def __init__(self, nm_cliente, ds_tipo_cliente_virtual,ds_rg_cliente, ds_senha_cliente_virtual, ds_cpf_cnpj_cliente, dt_nasc_cliente_virtual):
        self.nm_cliente = nm_cliente
        self.ds_tipo_cliente_virtual = ds_tipo_cliente_virtual
        self.ds_rg_cliente = ds_rg_cliente
        self.ds_senha_cliente_virtual = ds_senha_cliente_virtual
        self.ds_cpf_cnpj_cliente = Documento.cria_documento(ds_cpf_cnpj_cliente)
        self.dt_nasc_cliente_virtual = dt_nasc_cliente_virtual
        self.fl_cli_fis_vir = '1'
