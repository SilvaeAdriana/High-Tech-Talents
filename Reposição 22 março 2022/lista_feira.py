'''
Faça um programa que monte uma lista de compras na feira. Nesse programa deverá conter:
-Uma tela para mostrar a lista de compras
-Outra tela para cadastrar um item dessa lista
-Outra tela para excluir um item (Deverá primeiro mostrar a lista e depois excluir o item conforme posição)
-Login ao começar
-Opção Sair do programa
Dicas:
Use Lista
Não necessita de usar funções, mas pode usar se achar necessário
Não necessita criar classes, mas pode usar se achar necessário
Use como base, os exercicios anteriores para montar o programa (Tabuada e o do Troubleshooting feito em sala de aula)
Use funções de listas
Válido somente para quem faltou no kahoot da semana passada, mas se os outros quiserem fazer para treinar, fiquem a vontade
Entrega para próxima semana (04/04)



'''



# Nessa versão do programa, o item da lista é retirado conforme sua posição na lista
usuario = input("Entre com o seu nome: ")
print(f"Seja Bem-vindo {usuario} !\n")
print(f" Bora montar sua lista de compras para a feira?")
lista = []
while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Sair")
    opcao = int(input(""))
    if opcao in [1,2,3,4]:
        if opcao == 1: #Cadastrar
            nome_produto = ""
           
            while nome_produto == "":
                nome_produto = input("Coloque o nome do produto a ser inserido na lista: ")
           

            registro = nome_produto
            lista.append(registro)
            print("Sucesso! Produto cadastrado!")
        elif opcao == 2: #Listar
            for item in lista:
                print(item,'')
            
        elif opcao == 3:
            for item in lista:
                print(lista)
                fora = int(input("Digite a posição do produto a ser retirado da lista: "))
                del(lista[fora-1])
                print(f" A nova lista é:{lista}")
            
        elif opcao == 4: #Sair
            print("Saindo do sistema...")
            break
    else:
        print("Opção Inválida!") 