import cx_Oracle
from connection import conectar


class FuncionarioDAO:
    def __init__(self):
        self.conexao = conectar()

    def insert_funcionario(self, funcionario):
        cursor = self.conexao.cursor()
        cursor.callproc("system.pckg_funcionario_s_v_poo_ds.insert_funcionario", [
                funcionario['nm_funcionario'],
                funcionario['ds_cargo_funcionario'],
                funcionario['ds_cpf_funcionario'],
                funcionario['ds_rg_funcionario'],
                funcionario['dt_nascimento'],
                funcionario['dt_cadastro'],
                funcionario['sg_genero_funcionario']
        ])
        self.conexao.commit()
        cursor.close()
        
    def update_funcionario(self, funcionario):
        cursor = self.conexao.cursor()
        cursor.callproc("system.pckg_funcionario_s_v_poo_ds.update_funcionario", [
            funcionario.nm_funcionario,
            funcionario.ds_cargo_funcionario,
            funcionario.ds_cpf_funcionario,
            funcionario.ds_rg_funcionario,
            funcionario.dt_nascimento,
            None,
            funcionario.sg_genero_funcionario
        ])
        self.conexao.commit()
        cursor.close()

    def delete_funcionario(self, cd_funcionario):
        cursor = self.conexao.cursor()
        cursor.callproc("system.pckg_funcionario_s_v_poo_ds.delete_funcionario", [cd_funcionario])
        self.conexao.commit()
        cursor.close()
        

    def select_funcionarios(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT cd_funcionario, nm_funcionario FROM t_funcionario")
        result_set = cursor.fetchall()
        funcionarios = []
        for row in result_set:
            funcionario = {
                'cd_funcionario': row[0],
                'nm_funcionario': row[1]
            }
            funcionarios.append(funcionario)
        cursor.close()
        return funcionarios

    def select_funcionario_by_id(self, cd_funcionario):
        try:
                cursor = self.conexao.cursor()
                cur_out = cursor.var(cx_Oracle.CURSOR)
                cursor.callproc("system.pckg_funcionario_s_v_poo_ds.select_funcionario", [cd_funcionario, cur_out])
                
                result_set = cur_out.getvalue()
                funcionario = None
                
                for row in result_set:
                        funcionario = {
                                'cd_funcionario': row[0],
                                'nome': row[1],
                                'cpf': row[3],
                                'rg': row[4],
                                'genero': row[7]
                        }
                        break
                
                cursor.close()
                return funcionario
                
        except Exception as ex:
                print("Erro:", ex)