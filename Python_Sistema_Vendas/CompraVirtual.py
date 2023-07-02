class CompraVirtual:
    def __init__(self, cd_funcionario, cd_cliente, sg_status_entrega, ob_observacao, vl_desconto, vl_frete):
        self.cd_funcionario = cd_funcionario
        self.cd_cliente = cd_cliente
        self.sg_status_entrega = sg_status_entrega
        self.ob_observacao = ob_observacao
        self.vl_desconto = vl_desconto
        self.vl_frete = vl_frete
        self.fl_compra_fis_vir = '1'
