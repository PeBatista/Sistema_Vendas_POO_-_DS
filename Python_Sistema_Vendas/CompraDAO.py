import cx_Oracle
from connection import conectar


class CompraDAO:
    def __init__(self):
        self.conexao = conectar()

# TABELA COMPRA
    
        
    def insert_compra_fisico(self, compra):
        cursor = self.conexao.cursor()
        cursor.execute('BEGIN pckg_compra_s_v_poo_ds.insert_compra('
                    'p_cd_funcionario => :cd_funcionario, '
                    'p_cd_cliente => :cd_cliente, '
                    'p_vl_frete => :vl_frete); END;',
                    {
                        'cd_funcionario': compra.cd_funcionario,
                        'cd_cliente': compra.cd_cliente,
                        'vl_frete': compra.vl_frete
                    })
        self.conexao.commit()
        cursor.close()
        
    def insert_compra_virtual(self, compra):
        cursor = self.conexao.cursor()
        cursor.execute("""
            BEGIN
                pckg_compra_s_v_poo_ds.insert_compra(
                    p_cd_funcionario => :cd_funcionario,
                    p_cd_cliente => :cd_cliente,
                    p_sg_status_entrega => :sg_status_entrega,
                    p_ob_observacao => :ob_observacao,
                    p_vl_desconto => :vl_desconto,
                    p_vl_frete => :vl_frete,
                    p_fl_compra_fis_vir => :fl_compra_fis_vir
                );
            END;
        """,
        {
            'cd_funcionario': compra.cd_funcionario,
            'cd_cliente': compra.cd_cliente,
            'sg_status_entrega': compra.sg_status_entrega,
            'ob_observacao': compra.ob_observacao,
            'vl_desconto': compra.vl_desconto,
            'vl_frete': compra.vl_frete,
            'fl_compra_fis_vir': compra.fl_compra_fis_vir
        })
        self.conexao.commit()
        cursor.close()

    def delete_compra(self, cd_compra):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_compra_s_v_poo_ds.delete_compra', [cd_compra])
        self.conexao.commit()
        cursor.close()

    def update_compra(self, compra):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_compra_s_v_poo_ds.update_compra', [
            compra.cd_compra,
            compra.sg_status_entrega
        ])
        self.conexao.commit()
        cursor.close()

    def select_compra(self, cd_compra):
        cursor = self.conexao.cursor()
        cursor.execute('BEGIN pckg_compra_s_v_poo_ds.select_compra(:cd_compra, :cur_out); END;', {
            'cd_compra': cd_compra,
            'cur_out': cursor.var(cx_Oracle.CURSOR)
        })
        result_set = cursor.fetchone()

        if result_set:
            compra = Compra(
                cd_compra=result_set[0],
                cd_funcionario=result_set[1],
                cd_cliente=result_set[2],
                dt_hora_compra=result_set[3],
                sg_status_entrega=result_set[4],
                dt_data_entrega=result_set[5],
                ob_observacao=result_set[6],
                vl_desconto=result_set[7],
                vl_frete=result_set[8],
                fl_compra_fis_vir=result_set[9]
            )
            cursor.close()
            return compra

        cursor.close()
        return None
    
    def select_codigo_compra(self,cd_cliente, cd_funcionario):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT cd_compra FROM t_compra WHERE cd_cliente = :cd_cliente AND cd_funcionario = :cd_funcionario', 
                    cd_cliente=cd_cliente, cd_funcionario=cd_funcionario)
        codigos_compra = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return codigos_compra[0]
    
# TABELA PRODUTO_VENDIDO

    def insert_produto_vendido(self, produto_vendido):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_compra_s_v_poo_ds.insert_produto_vendido', [
            produto_vendido.cd_produto,
            produto_vendido.cd_compra,
            produto_vendido.ds_quantidade
        ])
        self.conexao.commit()
        cursor.close()

    def delete_produto_vendido(self, produto_vendido):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_compra_s_v_poo_ds.delete_produto_vendido', [
            produto_vendido.cd_produto,
            produto_vendido.cd_compra
        ])
        self.conexao.commit()
        cursor.close()

    def update_produto_vendido(self, produto_vendido):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_compra_s_v_poo_ds.update_produto_vendido', [
            produto_vendido.cd_produto,
            produto_vendido.cd_compra,
            produto_vendido.ds_quantidade
        ])
        self.conexao.commit()
        cursor.close()

    def select_produto_vendido(self, cd_produto, cd_compra):
        cursor = self.conexao.cursor()
        cur_out = cursor.var(cx_Oracle.CURSOR)
        cursor.callproc('pckg_compra_s_v_poo_ds.select_produto_vendido', [
            cd_produto,
            cd_compra,
            cur_out
        ])
        resultado = cur_out.getvalue().fetchall()
        cursor.close()
        return resultado
