'''
Faça um programa que peça as 4 notas bimestrais e mostre a média.
'''
print(42 * '*')
print('*** Calcula média ***')
nota1 = float(input('Digite aqui sua primeira nota bimestral: '))
nota2 = float(input('Digite aqui sua segunda nota bimestral: '))
nota3 = float(input('Digite aqui sua terceira nota bimestral: '))
nota4 = float(input('Digite aqui sua quarta nota bimestral: '))
media_notas = (nota1 + nota2 + nota3 + nota4)/4
print(f'A sua média no ano foi de {media_notas}')
print(42 * '*')