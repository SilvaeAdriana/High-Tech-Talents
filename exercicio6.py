'''
Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
'''
import cmath
raio = float(input('Digite o raio do círculo do qual você quer saber a área: '))
area = cmath.pi*(raio * raio)
print('A área do círculo com raio de {} é de {:.2f}.'.format(raio,area))