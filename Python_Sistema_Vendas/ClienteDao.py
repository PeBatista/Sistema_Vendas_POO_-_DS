import cx_Oracle
from connection import conectar

class ClienteDAO:
    def __init__(self):
        self.conexao = conectar()
        
    def insert_cliente_fisico(self, cliente):
        cursor = self.conexao.cursor()
        cursor.execute('BEGIN pckg_cliente_s_v_poo_ds.insert_cliente('
                    'p_nm_cliente => :nm_cliente, '
                    'p_ds_cpf_cnpj_cliente => :ds_cpf_cnpj_cliente); END;',
                    {
                        'nm_cliente': cliente.nm_cliente,
                        'ds_cpf_cnpj_cliente': cliente.ds_cpf_cnpj_cliente
                    })
        self.conexao.commit()
        cursor.close()

    def insert_cliente_virtual(self, cliente):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_cliente_s_v_poo_ds.insert_cliente', [
            cliente.nm_cliente,
            cliente.ds_tipo_cliente_virtual,
            cliente.ds_rg_cliente,
            cliente.ds_senha_cliente_virtual,
            str(cliente.ds_cpf_cnpj_cliente),
            cliente.dt_nasc_cliente_virtual,
            '1'
        ])
        self.conexao.commit()
        cursor.close()

    def insert_contato_cliente_virtual(self, contato):
        cursor = self.conexao.cursor()
        cursor.execute('BEGIN pckg_cliente_s_v_poo_ds.insert_contato_cliente_virtual('
                    'p_cd_cliente => :cd_cliente, '
                    'p_ds_endereco_cliente_virtual => :ds_endereco_cliente_virtual, '
                    'p_ds_bairro_cliente_virtual => :ds_bairro_cliente_virtual, '
                    'p_ds_compl_cliente_virtual => :ds_compl_cliente_virtual, '
                    'p_ds_estado_cliente_virtual => :ds_estado_cliente_virtual, '
                    'p_ds_cdde_cliente_virtual => :ds_cdde_cliente_virtual, '
                    'p_ds_cel_cliente_virtual => :ds_cel_cliente_virtual, '
                    'p_ds_cep_cliente_virtual => :ds_cep_cliente_virtual); END;',
                    {
                        'cd_cliente': contato.cd_cliente,
                        'ds_endereco_cliente_virtual': contato.ds_endereco_cliente_virtual,
                        'ds_bairro_cliente_virtual': contato.ds_bairro_cliente_virtual,
                        'ds_compl_cliente_virtual': contato.ds_compl_cliente_virtual,
                        'ds_estado_cliente_virtual': contato.ds_estado_cliente_virtual,
                        'ds_cdde_cliente_virtual': contato.ds_cdde_cliente_virtual,
                        'ds_cel_cliente_virtual': contato.ds_cel_cliente_virtual,
                        'ds_cep_cliente_virtual': contato.ds_cep_cliente_virtual
                    })
        self.conexao.commit()
        cursor.close()

    def delete_cliente(self, cd_cliente):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_cliente_s_v_poo_ds.delete_cliente', [cd_cliente])
        self.conexao.commit()
        cursor.close()

    def delete_contato_cliente_virtual(self, cd_contato_cliente_virtual):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_cliente_s_v_poo_ds.delete_contato_cliente_virtual', [cd_contato_cliente_virtual])
        self.conexao.commit()
        cursor.close()

    def update_cliente_fisico(self, cliente):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_cliente_s_v_poo_ds.update_cliente', [
            cliente.cd_cliente,
            cliente.nm_cliente,
            cliente.ds_tipo_cliente_virtual,
            cliente.ds_rg_cliente,
            cliente.ds_senha_cliente_virtual,
            cliente.ds_cpf_cnpj_cliente,
            cliente.dt_nasc_cliente_virtual,
            '0'
        ])
        self.conexao.commit()
        cursor.close()

    def select_clientes(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT cd_cliente, nm_cliente FROM t_cliente")
        result_set = cursor.fetchall()
        clientes = []
        for row in result_set:
            cliente = {
                'cd_cliente': row[0],
                'nm_cliente': row[1]
            }
            clientes.append(cliente)
        cursor.close()
        return clientes

    def update_cliente_virtual(self, cliente):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_cliente_s_v_poo_ds.update_cliente', [
            cliente.cd_cliente,
            cliente.nm_cliente,
            cliente.ds_tipo_cliente_virtual,
            cliente.ds_rg_cliente,
            cliente.ds_senha_cliente_virtual,
            cliente.ds_cpf_cnpj_cliente,
            cliente.dt_nasc_cliente_virtual,
            '1'
        ])
        self.conexao.commit()
        cursor.close()

    def update_contato_cliente_virtual(self, contato):
        cursor = self.conexao.cursor()
        cursor.callproc('pckg_cliente_s_v_poo_ds.update_contato_cliente_virtual', [
            contato.cd_contato_cliente_virtual,
            contato.cd_cliente,
            contato.ds_endereco_cliente_virtual,
            contato.ds_bairro_cliente_virtual,
            contato.ds_compl_cliente_virtual,
            contato.ds_estado_cliente_virtual,
            contato.ds_cdde_cliente_virtual,
            contato.ds_cel_cliente_virtual,
            contato.ds_cep_cliente_virtual
        ])
        self.conexao.commit()

