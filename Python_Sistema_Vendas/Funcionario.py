from Documento_CNPJ_CPF import Documento


class Funcionario:
    def __init__(self, nm_funcionario, ds_cargo_funcionario, ds_cpf_funcionario, ds_rg_funcionario, dt_nascimento, sg_genero_funcionario):
        self.nm_funcionario = nm_funcionario
        self.ds_cargo_funcionario = ds_cargo_funcionario
        self.ds_cpf_funcionario = Documento.cria_documento(ds_cpf_funcionario)
        self.ds_rg_funcionario = ds_rg_funcionario
        self.dt_nascimento = dt_nascimento
        self.sg_genero_funcionario = sg_genero_funcionario