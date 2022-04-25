'''
A aplicação feita em Console, com os 4 objetos de negócio principais: Inquilino, Proprietario, Imóvel, Aluguel.
Simulação de cadastro de uma imobiliária.
Utilizando classes do Python para criar uma lista de objetos dessas classes.
'''


from classes import Aluguel,Inquilino,Imovel,Proprietario
import os
import csv

resposta = 'sim'
while resposta == 'sim':
    os.system('cls') or None


    print('********* Aluguel **************')
    print('Escolha sua opção:')
    print("""
        [1] Inquilino\n
        [2] Proprietário\n
        [3] Imóvel\n
        [4] Aluguel""")
    opcao = int(input('\n Escolha uma opção: '))
    if opcao == 1:
        print("""
        [1] Cadastrar Inquilino\n
        [2] Mostrar Inquilinos\n
        [3] Mostrar Dados de Inquilino Específico""")
        escolha=int(input('\n Escolha uma opção: '))
        if escolha == 1:
            Inquilino.cadastrar_inquilino()
        elif escolha == 2:
            Inquilino.mostrar_inquilino()
        elif escolha == 3:
            Inquilino.mostra_reg_inquilino()
        else:
            print('Opção inválida, escolha uma entre as opções acima.')

    elif opcao == 2:
        print("""
        [1] Cadastrar Proprietário\n
        [2] Mostrar Proprietários\n
        [3] Mostrar Dados de Proprietário Específico""")
        escolha=int(input('\n Escolha uma opção: '))
        if escolha == 1:
            Proprietario.cadastrar_proprietario()
        elif escolha == 2:
            Proprietario.mostrar_proprietario()            
        elif escolha == 3:
            Proprietario.mostra_reg_proprietario()
        else:
            print('Opção inválida, escolha uma entre as opções acima.')

    elif opcao == 3:
        print("""
        [1] Cadastrar Imóvel\n
        [2] Mostrar Imóveis\n
        [3] Mostrar Dados de Imóvel Específico""")
        escolha=int(input('\n Escolha uma opção: '))
        if escolha == 1:
            Imovel.cadastrar_imovel()
        elif escolha == 2:
            Imovel.mostrar_imovel()
        elif escolha == 3:
            Imovel.mostra_reg_imovel()
        else:
            print('Opção inválida, escolha uma entre as opções acima.')  

    elif opcao == 4:
        print("""
        [1] Cadastrar Aluguel\n
        [2] Mostrar Aluguéis\n
        [3] Mostrar Dados de Aluguel Específico""")
        escolha=int(input('\n Escolha uma opção: '))
        if escolha == 1:
            Aluguel.cadastrar_aluguel()
        elif escolha == 2:
            Aluguel.mostrar_aluguel()
        elif escolha == 3:
            Aluguel.mostra_reg_aluguel()
        else:
            print('Opção inválida, escolha uma entre as opções acima.')
    
    resposta = input('Deseja continuar? [sim/não]')

print( 'Fim')
    