"""
Exercícios da seção 4, questões de 33 a 36
"""
import math # Adicionei para poder usar a função na questão 35
pi = 3.141592


# 33. Leia o tamanho do lado de um quadrado e imprima como resultado a sua área
lado = float(input('Informe o tamanho de um lado do quadrado: \n '))
print(f'A área do quadrado informado é {lado ** 2}')


# 34. Leia o valor do raio de um círculo e calcule e imprima a área do círculo.
raio = float(input('Informe o raio do círculo: \n '))
print(f'A área do círculo informado é {round(pi * raio ** 2, 2)}')


# 35. Faça um programa que receba os valores a e b e calcule o valor da hipotenusa.
a = float(input('Digite o valor de a: \n'))
b = float(input('Digite o valor de b: \n'))
print(f'Com os valores informados temos uma hipotenusa igual a: {round(math.sqrt(a ** 2 + b ** 2), 2)}')
# Tive que adicionar o import math no início para conseguir usar a função


# 36. Leia o raio de um cilindro circular e imprima o volume do cilindro
altura = float(input('Digite a altura do cilindro: \n'))
raio = float(input('Digite o raio do cilindro: \n'))
print(f'O volume do cilindro é: {round(pi * raio ** 2 * altura, 2)}')
