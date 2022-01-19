"""
Exercícios da seção 5, questões de 1 a 5
"""
import math
# 1. Faça um programa que receba dois números e mostre qual o maior.
# a, b = input('Informe os dois numeros: ').split(" ")
a = input('Informe o primeiro número: ')
b = input('Informe o segundo número: ')
if a > b:
    print(f'{a} é o maior')
elif a == b:
    print('Números iguais')
else:
    print(f'{b} é o maior')


# 2. Leia um número fornecido pelo usuário
"""
Se o número for positivo, calcule a raiz quadrada do número
Se o número for negativo, mostre uma mensagem informando que o número é inválido
"""
a = float(input('Informe o número: '))
if a >= 0:
    print(f'A raiz quadrada de {a} é {a ** 0.5}')
    print(f'A raiz quadrada de {a} é {math.sqrt(a)}')
else:
    print('Número inválido')


# 3. Leia um número real
"""
Se o número for positivo, imprima a raiz quadrada do número. Do contrário, imprima o número ao quadrado
"""
x = float(input('Digite o número: '))
if x >= 0:
    print(f'A raiz quadrada de {x} é {x ** 0.5}')
    print(f'A raiz quadrada de {x} é {math.sqrt(x)} ')
else:
    print(f'O quadrado de {x} é {x ** 2}')


# 4. Leia um número e, caso ele se positivo, calcule e mostre:
"""
1 - O número digitado ao quadrado
2 - A raiz quadrada do número digitado
"""
x = float(input('Digite o número: '))
if x >= 0:
    print(f'A raiz quadrada de {x} é {x ** 0.5}')
    print(f'A raiz quadrada de {x} é {math.sqrt(x)} ')
    print(f'O quadrado de {x} é {x ** 2}')
else:
    print(f'Números negativo')


# 5. Receba um número inteiro e verifique se este número é par ou ímpar
x = int(input('Digite um número inteiro: '))
if x % 2 == 0:
    print(f'O número {x} é par')
else:
    print(f'O número {x} é ímpar')
