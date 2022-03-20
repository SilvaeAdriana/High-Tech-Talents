'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhads no mês. Clacule e mostre o total do seu salário no referido mês.
'''
print(48 * '*')
print('*** Calcule seu salário mensal. ***')
valor = float(input('Digite aqui qual valor em reais você recebe por hora: '))
horas = float(input('Digite aqui quantas horas você trabalhou nesse mês: '))
salario = valor * horas
print('Você trabalhou um total de {:.2f} horas nesse mês e receberá um salário de {:.2f}.'.format(horas,salario))
print(48 * '*')