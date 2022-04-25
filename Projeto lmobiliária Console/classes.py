import os
import csv



# O programa ainda leva em consideração que os ids são designados a cada usuário da tabela por ordem crescente


class Inquilino:

    def cadastrar_inquilino():
        dados = {}
        id = int(input('Digite o ID do cliente: '))
        nome = input("Nome: ")
        data_nasc  = input("Data de nascimento: ")
        endereco   = input("Endereço: ")                     
        colunas = ['id', 'nome', 'data de nascimento', 'endereço']
        file_exists = os.path.isfile('inquilino.csv')
        with open('inquilino.csv', 'a', newline='', encoding="utf8") as inquilino_csv:
            cadastrar = csv.DictWriter(inquilino_csv, fieldnames=colunas, delimiter=';', lineterminator='\r\n')
            if not file_exists:
                cadastrar.writeheader()
            cadastrar.writerow({'id':id, 'nome':nome, 'data de nascimento': data_nasc,'endereço': endereco})
        
        print('Cadastro realizado com sucesso!')



    def mostrar_inquilino():
        inquilino_csv = open('inquilino.csv')
        dados = csv.DictReader(inquilino_csv, delimiter = ';')        
        os.system('cls') or None
        print('-------------------------------------------------------')
        print('LISTAGEM DE INQUILINOS')
        print('-------------------------------------------------------')
        print(f'{"id":15}', f'{"nome":25}',f'{"data_nasc":15}',"endereco")
        for inquilino in dados:
            print(f'{inquilino["id"]:15}', f'{ inquilino["nome"]:25}', f'{inquilino["data_nasc"]:15}', inquilino["endereco"]) # objetos
        inquilino_csv.close()
        print('-------------------------------------------------------')



    def mostra_reg_inquilino():
        with open ('inquilino.csv',"r",encoding="utf8") as file:
            numero_linha=(int(input("Digite o número da linha a exibir: ")))
            for i, linha in enumerate(file,start=1):
                if i == numero_linha:
                    print( linha.split())






class Proprietario:

    def cadastrar_proprietario():
        dados = {}
        id = int(input('Digite o ID do cliente: '))
        nome = input("Nome: ")
        data_nasc  = input("Data de nascimento: ")
        endereco   = input("Endereço: ")
        colunas = ['id', 'nome', 'data de nascimento', 'endereco']
        file_exists = os.path.isfile('proprietario.csv')
        with open('proprietario.csv', 'a', newline='', encoding="utf8") as proprietario_csv:
            cadastrar = csv.DictWriter(proprietario_csv, fieldnames=colunas, delimiter=';', lineterminator='\r\n')
            if not file_exists:
                cadastrar.writeheader()
            cadastrar.writerow({'id':id, 'nome':nome, 'data de nascimento': data_nasc,'endereco': endereco})
        
        print('Cadastro realizado com sucesso!')



    def mostrar_proprietario():
        proprietario_csv = open('proprietario.csv')
        dados = csv.DictReader(proprietario_csv, delimiter = ';')       
        os.system('cls') or None
        print('-------------------------------------------------------')
        print('LISTAGEM DE PROPRIETÁRIOS')
        print('-------------------------------------------------------')
        print(f'{"id":15}', f'{"nome":25}',f'{"data de nascimento":15}',"endereco")
        for proprietario in dados:
            print(f'{proprietario["id"]:15}', f'{ proprietario["nome"]:25}', f'{proprietario["data de nascimento"]:15}', proprietario["endereco"]) # objetos
        proprietario_csv.close()
        print('-------------------------------------------------------')



    def mostra_reg_proprietario():
        with open ('proprietario.csv',"r",encoding="utf8") as file:
            numero_linha=(int(input("Digite o número da linha a exibir: ")))
            for i, linha in enumerate(file,start=1):
                if i == numero_linha:
                    print( linha.split())




class Imovel:
    
    def cadastrar_imovel():
        dados = {}
        id = int(input('Digite o ID do imóvel: '))
        logradouro = input("Logradouro: ")
        cep  = input("CEP: ")
        bairro   = input("Bairro: ")
        cidade = input("Cidade: ")
        id_proprietario = int(input("ID do proprietário: "))
        colunas = ['id', 'logradouro','cep','bairro','cidade','id_proprietario']
        file_exists = os.path.isfile('imovel.csv')
        with open('imovel.csv', 'a', newline='') as imovel_csv:
            cadastrar = csv.DictWriter(imovel_csv, fieldnames=colunas, delimiter=';', lineterminator='\r\n')
            if not file_exists:
                cadastrar.writeheader()
            cadastrar.writerow({'id':id, 'logradouro': logradouro, 'cep': cep,'bairro':bairro, 'cidade': cidade, 'id_proprietario': id_proprietario}) # em branco, as variaveis, em amarelo-colunas
        
        print('Cadastro realizado com sucesso!')



    def mostrar_imovel():
        imovel_csv = open('imovel.csv')
        dados = csv.DictReader(imovel_csv, delimiter = ';')        
        os.system('cls') or None
        print('-------------------------------------------------------')
        print('LISTAGEM DE IMÓVEIS')
        print('-------------------------------------------------------')
        print(f'{"id":15}', f'{"logradouro":25}',f'{"cep":15}',f'{"bairro":15}',f'{"cidade":25}',"id_proprietario")
        for imovel in dados:
            print(f'{imovel["id"]:15}', f'{imovel["logradouro"]:25}', f'{imovel["cep"]:15}',imovel["id_proprietario"]) # objetos
        imovel_csv.close()
        print('-------------------------------------------------------')



    def mostra_reg_imovel():
        with open ('imovel.csv',"r",encoding="utf8") as file:
            numero_linha=(int(input("Digite o número da linha a exibir: ")))
            for i, linha in enumerate(file,start=1):
                if i == numero_linha:
                    print( linha.split())




class Aluguel:
    
    def cadastrar_aluguel():
        dados = {}
        id_aluguel = int(input(" Digite o ID do aluguel: "))
        id_imovel = int(input("ID do imovel: "))
        id_inquilino = int(input("ID do inquilino: "))
        colunas = ['id_aluguel', 'id_imovel', 'id_inquilino']
        file_exists = os.path.isfile('aluguel.csv')
        with open('aluguel.csv', 'a', newline='', encoding="utf8") as aluguel_csv:
            cadastrar = csv.DictWriter(aluguel_csv, fieldnames=colunas, delimiter=';', lineterminator='\r\n')
            if not file_exists:
                cadastrar.writeheader()
            cadastrar.writerow({'id_aluguel':id_aluguel,'id_imovel': id_imovel, 'id_inquilino': id_inquilino}) # em branco, as variaveis, em amarelo-colunas
        
        print('Cadastro realizado com sucesso!')



    def mostrar_aluguel():
        aluguel_csv = open('aluguel.csv')
        dados = csv.DictReader(aluguel_csv, delimiter = ';')       
        os.system('cls') or None
        print('-------------------------------------------------------')
        print('LISTAGEM DE ALUGUÉIS')
        print('-------------------------------------------------------')
        print(f'{"id_aluguel":15}', f'{"id_imovel":25}',"id_inquilino")        
        for aluguel in dados:
            print(f'{aluguel["id_aluguel"]:15}', f'{aluguel["id_imovel"]:25}', aluguel["id_inquilino"]) # objetos
        aluguel_csv.close()
        print('-------------------------------------------------------')


    
    # COMO LER UMA LINHA ESPECÍFICA
    def mostra_reg_aluguel():
        with open ('clientes.csv',"r",encoding="utf8") as file:
            numero_linha=(int(input("Digite o número da linha a exibir: ")))
            for i, linha in enumerate(file,start=1):
                if i == numero_linha:
                    print( linha.split())



    # DELETA A TABELA TODA
    def deletar_aluguel(): #troquei txt por csv e funcionou, antes baixei uma extesnsão chamada EXCEL VIEWER e não sei se tem relação, DELETA TODA A TABELA

        with open("aluguel.csv","r") as f:
            lines = f.readlines()
        with open("aluguel.csv", "a") as f:
            print('Escolha a linha a ser deletada a partir da linha 2: ')
            linha=int(input('Digite a linha: '))
            for line in lines:
                if line.strip == linha and line.strip != 1: # acata apenas line, contudo também exclui toda a tabela  
                    # com != replica a tabela
                    f.write(line)
                    print('Feito!')




