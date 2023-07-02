import cx_Oracle


def conectar():
        # Configuração da conexão
        user = 'system'
        password = 'admin'
        dsn = 'localhost:1521/xe'

        # Cria a conexão
        connection = cx_Oracle.connect(user, password, dsn)
        return connection




