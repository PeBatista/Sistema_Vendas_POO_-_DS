import cx_Oracle
from connection import conectar

class FornecedorDAO:
    def __init__(self):
        self.conexao = conectar()

    def insert_fornecedor(self, fornecedor):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_fornecedor_s_v_poo_ds.insert_fornecedor', [
            fornecedor.nm_fornecedor,
            fornecedor.ds_cpf_fornecedor,
            fornecedor.ds_rg_fornecedor,
            fornecedor.sg_genero_fornecedor,
            fornecedor.dt_cadastro_fornecedor
        ])
        self.conexao.commit()
        cursor.close()

    def insert_contato_fornecedor(self, contato):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_fornecedor_s_v_poo_ds.insert_contato_fornecedor', [
            contato.cd_fornecedor,
            contato.ds_telefone_fornecedor,
            contato.ds_cel_fornecedor,
            contato.ds_endereco_moradia_empresa
        ])
        self.conexao.commit()
        cursor.close()

    def delete_fornecedor(self, cd_fornecedor):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_fornecedor_s_v_poo_ds.delete_fornecedor', [cd_fornecedor])
        self.conexao.commit()
        cursor.close()

    def delete_contato_fornecedor(self, cd_contato_fornecedor):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_fornecedor_s_v_poo_ds.delete_contato_fornecedor', [cd_contato_fornecedor])
        self.conexao.commit()
        cursor.close()

    def update_fornecedor(self, fornecedor):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_fornecedor_s_v_poo_ds.update_fornecedor', [
            fornecedor.cd_fornecedor,
            fornecedor.nm_fornecedor,
            fornecedor.ds_cpf_fornecedor,
            fornecedor.ds_rg_fornecedor,
            fornecedor.sg_genero_fornecedor,
            fornecedor.dt_cadastro_fornecedor
        ])
        self.conexao.commit()
        cursor.close()

    def update_contato_fornecedor(self, contato):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_fornecedor_s_v_poo_ds.update_contato_fornecedor', [
            contato.cd_contato_fornecedor,
            contato.cd_fornecedor,
            contato.ds_telefone_fornecedor,
            contato.ds_cel_fornecedor,
            contato.ds_endereco_moradia_empresa
        ])
        self.conexao.commit()
        cursor.close()

    def select_fornecedor(self, cd_fornecedor):
        cursor = self.conexao.cursor()
        cur_out = cursor.var(cx_Oracle.CURSOR)
        cursor.callproc('pckg_fornecedor_s_v_poo_ds.select_fornecedor', [cd_fornecedor, cur_out])
        result = cur_out.getvalue().fetchall()
        cursor.close()
        return result

    def select_contato_fornecedor(self, cd_contato_fornecedor):
        cursor = self.conexao.cursor()
        cur_out = cursor.var(cx_Oracle.CURSOR)
        cursor.callproc('pckg_fornecedor_s_v_poo_ds.select_contato_fornecedor', [cd_contato_fornecedor, cur_out])
        result = cur_out.getvalue().fetchall()
        cursor.close()
        return result

    