
from BuscaEndereco import BuscaEndereco

class ContatoClienteVirtual:
    def __init__(self, cd_cliente, ds_cep_cliente_virtual, ds_cel_cliente_virtual):
        cep = BuscaEndereco(ds_cep_cliente_virtual)
        dados_endereco = cep.acessa_via_cep()

        self.cd_cliente = cd_cliente
        self.ds_endereco_cliente_virtual = dados_endereco['logradouro']
        self.ds_bairro_cliente_virtual = dados_endereco['bairro']
        self.ds_compl_cliente_virtual = dados_endereco['ibge']
        self.ds_estado_cliente_virtual = dados_endereco['uf']
        self.ds_cdde_cliente_virtual = dados_endereco['localidade']
        self.ds_cel_cliente_virtual = ds_cel_cliente_virtual
        self.ds_cep_cliente_virtual = str(cep)
