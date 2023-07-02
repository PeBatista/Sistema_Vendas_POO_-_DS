# FUNÇÃO QUAL O SEU ID?

            
from FuncionarioDAO import FuncionarioDAO
from ClienteDao import ClienteDAO
from ProdutoDao import ProdutoDAO
from CompraDAO import CompraDAO
from ClienteVirtual import ClienteVirtual
from CompraVirtual import CompraVirtual
from CompraFisica import CompraFisica
from ClienteFisico import ClienteFisico
from ContatoClienteVirtual import ContatoClienteVirtual
from ProdutoVendido import ProdutoVendido

def pergunta_id_funcionario():
    funcionario_dao = FuncionarioDAO()

    # Selecionar todos os funcionários
    funcionarios = funcionario_dao.select_funcionarios()

    # Exibir lista de funcionários com seus IDs
    for funcionario in funcionarios:
        print(f"ID: {funcionario['cd_funcionario']}, Nome: {funcionario['nm_funcionario']}")

    # Obter ID do funcionário selecionado
    id_funcionario = int(input("Qual funcionário é você? Digite o ID: "))

    # Selecionar o funcionário escolhido pelo ID
    funcionario_escolhido = funcionario_dao.select_funcionario_by_id(id_funcionario)

    # Exibir informações do funcionário escolhido
    if funcionario_escolhido:
        print("\nInformações do funcionário escolhido:")
        print(f"ID: {funcionario_escolhido['cd_funcionario']}")
        print(f"Nome: {funcionario_escolhido['nome']}")
        print(f"CPF: {funcionario_escolhido['cpf']}")
        print(f"RG: {funcionario_escolhido['rg']}")
        print(f"Gênero: {funcionario_escolhido['genero']}")
    else:
        print(f"\nFuncionário com ID {id_funcionario} não encontrado.")
    
    return id_funcionario

def virtual(cd_funcionario):
    # exemplo de dados quando Compra Virtual
    cliente = ClienteVirtual("Victor da Batista", "Premium", "12345678", "senha123", "12345678900", "18/06/2023")
    # instânciando a DAO e chamando o insert do cliente quando virtual
    cliente_dao = ClienteDAO()
    cliente_dao.insert_cliente_virtual(cliente)
    clientes = cliente_dao.select_clientes()
    
    for cliente in clientes:
        print(f"ID: {cliente['cd_cliente']} - Nome: {cliente['nm_cliente']}")
    
    cd_cliente = int(input('Que Cliente você deseja cadastrar:'))

    # Chame o método insert_contato_cliente_virtual e passe o objeto contato como argumento
    
    contato_cliente_virtual = ContatoClienteVirtual(cd_cliente, '01007020', '1198874498')
    
    cliente_dao.insert_contato_cliente_virtual(contato_cliente_virtual)

    compra = CompraVirtual(cd_funcionario, cd_cliente, 'N', 'Observação 2', 1, 15.5)
    
    compra_dao = CompraDAO()
    compra_dao.insert_compra_virtual(compra)
    cd_compra = compra_dao.select_codigo_compra(cd_cliente, cd_funcionario) # código da compra para adicionar na tabela de produto vendido 
    
    
    
    produto_dao = ProdutoDAO()
    produtos = produto_dao.select_produtos()
    
    # dar INSERTS dentro do BD para testar a PROC de produtos.
    
    while True:
        for produto in produtos:
            print(f"ID: {produto['cd_produto']} - Nome: {produto['nm_produto']}")
        
        cd_produto = int(input("Digite o ID do produto desejado: "))
        
        produto_vendido = ProdutoVendido(cd_produto,cd_compra,2)
        
        compra_dao.insert_produto_vendido(produto_vendido)
        
        resposta = input("Deseja adicionar mais algum produto? (s/n): ")
        if resposta.lower() not in ['s', 'sim']:
            break
    
    
def fisico(cd_funcionario):
    # exemplo de dados quando compra Fisica
    cliente = ClienteFisico('Mike', '04458000')
    
    # instânciando a DAO e chamando o insert do cliente quando fisico
    cliente_dao = ClienteDAO()
    cliente_dao.insert_cliente_fisico(cliente)
    clientes = cliente_dao.select_clientes()

    
    for cliente in clientes:
        print(f"ID: {cliente['cd_cliente']} - Nome: {cliente['nm_cliente']}")
    
    cd_cliente = int(input('Que Cliente você deseja cadastrar:'))
    
    compra = CompraFisica(cd_funcionario, cd_cliente, 1.5, 15.5)
    
    compra_dao = CompraDAO()
    compra_dao.insert_compra_fisico(compra)
    cd_compra = compra_dao.select_codigo_compra(cd_cliente, cd_funcionario) # código da compra para adicionar na tabela de produto vendido 
    
    produto_dao = ProdutoDAO()
    produtos = produto_dao.select_produtos()
    
    # dar INSERTS dentro do BD para testar a PROC de produtos.
    
    while True:
        for produto in produtos:
            print(f"ID: {produto['cd_produto']} - Nome: {produto['nm_produto']}")
        
        cd_produto = int(input("Digite o ID do produto desejado: "))
        
        produto_vendido = ProdutoVendido(cd_produto,cd_compra,2)
        
        compra_dao.insert_produto_vendido(produto_vendido)
        
        resposta = input("Deseja adicionar mais algum produto? (s/n): ")
        if resposta.lower() not in ['s', 'sim']:
            break
    
    
    
        
    
while True:
        id_funcionario = pergunta_id_funcionario()

        tipo_compra = input("A compra a ser realizada é física ou virtual? (F/V): ")

        if tipo_compra.upper() == "F":
            fisico(id_funcionario)
        elif tipo_compra.upper() == "V":
            virtual(id_funcionario)
        else:
            print("Opção inválida.")

        resposta = input("Deseja sair do programa ou realizar mais uma compra? (Sair/Compra): ")
        if resposta.lower() == "sair":
            break

print("Obrigado Por Usar meu Programa POO com Python e Oracle PL-SQL")
print("Nome: Pedro Batista Mendonça")
print("Data: 20/06/2023")   
print("e-mail: pedrobatista242526@gmail.com")         