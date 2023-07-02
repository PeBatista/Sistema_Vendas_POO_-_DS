import cx_Oracle
from connection import conectar

class ProdutoDAO:
    def __init__(self):
        self.conexao = conectar()

    def insert_produto(self, produto):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_produto_s_v_poo_ds.insert_produto', [
            produto.cd_fornecedor,
            produto.nm_produto,
            produto.ds_produto,
            produto.vl_preco,
            None,
            produto.ds_fabricante,
            produto.ds_grupo,
            produto.nr_estoque
        ])
        self.conexao.commit()
        cursor.close()

    def delete_produto(self, cd_produto):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_produto_s_v_poo_ds.delete_produto', [cd_produto])
        self.conexao.commit()
        cursor.close()

    def update_produto(self, produto):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_produto_s_v_poo_ds.update_produto', [
            produto.cd_produto,
            produto.cd_fornecedor,
            produto.nm_produto,
            produto.ds_produto,
            produto.vl_preco,
            produto.ds_ativo,
            produto.ds_fabricante,
            produto.ds_grupo,
            produto.nr_estoque
        ])
        self.conexao.commit()
        cursor.close()

    def select_produto(self, cd_produto):
        cursor = self.conexao.cursor()
        cur_out = cursor.var(cx_Oracle.CURSOR)
        cursor.callproc('pckg_produto_s_v_poo_ds.select_produto', [cd_produto, cur_out])
        result = cur_out.getvalue().fetchall()
        cursor.close()
        return result

    def select_produtos(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT cd_produto, nm_produto FROM t_produto")
        result_set = cursor.fetchall()
        produtos = []
        for row in result_set:
            produto = {
                'cd_produto': row[0],
                'nm_produto': row[1]
            }
            produtos.append(produto)
        cursor.close()
        return produtos
