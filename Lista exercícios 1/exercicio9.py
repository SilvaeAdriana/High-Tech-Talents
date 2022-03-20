'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.C = 5 * ((F-32) / 9).
'''
print(48 * '*')
print('*** Conversor de temperatura: Fahrenheit --> Celsius. ***')
fahrenheit = float(input('Digite aqui a temperatura em Fahrenheit que você quer converter em Celsius: '))
celsius = 5 * ((fahrenheit-32)/9)
print('A temperatura de {:.2f} Fahrenheit corresponde a {:.2f} Celsius.'.format(fahrenheit, celsius))
print(48 * '*')