"""
Exercícios da seção 4, questões de 28 a 32
"""
# 28. Faça a leitura de 3 valores e apresente como resultado a soma dos quadrados dos 3 valores lidos
print('Informe 3 valores')
a = int(input('Digite o primeiro valor '))
b = int(input('Digite o segundo valor '))
c = int(input('Digite o terceiro valor '))
print(f'A soma do quadrados do 3 valores é {a**2 + b**2 + c**2}')


# 29. Leia 4 notas, calcule a média aritmética e imprmia o resultado
print('Informe o valor das 4 notas')
a = int(input('Nota 1 '))
b = int(input('Nota 2 '))
c = int(input('Nota 3 '))
d = int(input('Nota 4 '))
print(f'A média aritimética das notas é {float((a + b + c + d) / 4)}')


# 30. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares
a = float(input('Valor em reais '))
dolar = 5.65
print(f'A cotação atual do dólar é {dolar}, você tem {a / dolar:0.3} em dolares')


# 31. Leia um número inteiro e imprima o seu antecessor e o seu sucessor
a = int(input('Digite um número inteiro '))
print(f'A sequência com antecessor e sucessor de {a} é... {a - 1}, {a} e {a + 1}')


# 32. Lei um números inteiro e imprima a soma do sucessor de seu triplo com antecessor de seu dobro
b = int(input('Digite um número inteiro '))
print(f'A soma do sucessor de seu triplo que é {b * 3 + 1}, com antecessor de seu dobro que é {b * 2 - 1} '
      f'é igual a {(b * 3 + 1) + (b * 2 - 1)}')
