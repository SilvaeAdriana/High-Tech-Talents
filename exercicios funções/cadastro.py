# Fazer um cadastro de 3 campos e guarda-lo em 
# um dicionário (Console)
# 1-) Entender o problema
# 2-) Planejar a solução
# -Criar um menu no console com 3 opções: 
#   - Sair 
#   - Cadastrar 
#   - Listar
# 3-) Dividir/Planejar Tarefas
#   - Preparar um arquivo Python (Este aqui mesmo)
#   - Criar Loop para o menu principal
#   - Criar "Tela" Cadastrar 
#       -Perguntar campo Nome
#       -Perguntar campo Data Nascimento
#       -Perguntar campo Endereço
#   - Criar "Tela" Listar
#       -Preparar Prints Dicionario
#   - Criar Funcionalidade Sair    
# 4-) Estimar tempo de desenvolvimento (Até o final da aula)

# script dadousuario = input("Entre com o seu nome: ")

'''
print(f"Seja Bem-vindo {usuario} !\n")
lista = []
while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")
    opcao = int(input(""))
    if opcao in [1,2,3]:
        if opcao == 1: #Cadastrar
            nome = ""
            data_nasc = ""
            endereco = ""
            while nome == "":
                nome = input("Coloque o nome: ")
            while data_nasc == "":
                data_nasc = input("Coloque a data de nascimento: ")
            while endereco == "":
                endereco = input("Coloque o endereço: ")

            registro = {"Nome":nome, "Data_Nascimento":data_nasc, "Endereco": endereco}
            lista.append(registro)
            print("Sucesso! Cadastrado!")
        elif opcao == 2: #Listar
            for item in lista:
                print(item)
            
        elif opcao == 3:#Sair
            print("Saindo do sistema...")
            break
    else:
        print("Opção Inválida!") pelo professor
'''

def menu():
    print("Selecione uma opção:")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")


    

def cadastrar():
    nome = ""
    data_nasc = ""
    endereco = ""       
    while nome == "":
        nome = input("Coloque o nome: ")
    while data_nasc == "":
        data_nasc = input("Coloque a data de nascimento: ")
    while endereco == "":
        endereco = input("Coloque o endereço: ")
    registro = {"Nome":nome, "Data_Nascimento":data_nasc, "Endereco": endereco}
    lista.append(registro)
    print("Sucesso! Cadastrado!")



def listar():
    for item in lista:
        print(item)

def sair():
    print("Saindo do sistema...")

def aviso():
    print("Opção Inválida!")

usuario = input("Entre com o seu nome: ")
print(f"Seja Bem-vindo {usuario} !\n")
lista = []
while True:
    menu()
    opcao = int(input("")) 
    if opcao in [1,2,3]:
        
        if opcao == 1: #Cadastrar
            cadastrar()
                        
        elif opcao == 2: #Listar
            listar()
            
        elif opcao == 3:#Sair
            sair()
            break
    else:
        aviso()