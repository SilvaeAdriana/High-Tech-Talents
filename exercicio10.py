'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''
print(48 * '*')
print('*** Conversor de temperatura: Celsius --> Fahrenheit. ***')
celsius = float(input('Digite aqui a temperatura em Celsius que você quer converter em Fahrenheit: '))
fahrenheit = ((celsius/5) * 9) + 32
print('A temperatura de {:.2f} Celsius corresponde a {:.2f} Fahrenheit.'.format(celsius,fahrenheit))