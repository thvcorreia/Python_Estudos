"""
Exercícios da seção 4, questões de 44 a 50
"""
import time

# 44. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule
# mostre quantos degraus o usuário deverá subir para alcançar o seu objetivo.
escada = float(input('Informe a altura de cada degrau da escada em metros: \n'))
altura = float(input('Informe a altura que você deseja chegar: \n'))
print(f'Para chagar a altura desejada vc deverá subir {round(altura / escada, 2)} degraus')


# 45. Faça um programa para converte um letra maiúscula em minúscula. Use a tabela ASCII para resolver o problema.
letra = input('Digite um letra maiúscula: \n')
# print(f'{ord(letra)}')  - Mostra qual o número da letra na tabela ASCII
# print(letra.lower())  - Converte a letra para minúsculo
# print(f'{ord(letra.lower())}') Mostra qual o número da letra na tabela ASCII convertida em minúsculo
print(f'A correspondente minúscula é: \n{chr(ord(letra) + 32)}')
# Desta forma consigo pegar qualquer letra Maiúscula e converte para Minúscula usando a tabela ASCII


# 46. Faça um programa que leia um número inteiro e positivo de 100 a 999 e o inverta
numero_lido = input('Digite um numero inteiro e positivo entre 100 e 999: \n')
numero_lido.isdigit()
print(f'O numero informada invertido é: \n{numero_lido[::-1]}')


# 47. Leia um número de 4 dígitos entre 1000 e 9999 e imprima um dígito por linha
numero_lido = input('Digite um numero inteiro e positivo entre 1000 e 9999: \n')
print(numero_lido[0])
print(numero_lido[1])
print(numero_lido[2])
print(numero_lido[3])


# 48. Leia um valor inteiro em segundos e imprima-o em hora, minutos e segundos
numero = int(input('Digite a quantidade de segundos desejada: '))
print(f'São {int(numero / 3600)}:{int((numero % 3600) / 60)}:{(numero % 3600) % 60}')
print(f'{time.strftime("%H:%M:%S", time.gmtime(numero))}')


# 49. Leia um horário de início e a duração, em segundos, de uma experiência biológica, retorne o novo horário
print('Informe a hora de início da experiência: \n')
h = int(input('Digite a hora: '))
m = int(input('Digite a minuto: '))
s = int(input('Digite a segundo: '))
print(f'{h}:{m}:{s}')
segundos_inicio = h * 3600 + m * 60 + s
duracao = int(input('Informe quanto segundos durou a experiência: '))
segundos_final = segundos_inicio + duracao
print(f'O exepriência terminou às: {time.strftime("%H:%M:%S", time.gmtime(segundos_final))}')


# 50. Implemente um programa que calcule o ano de nascimento de um pessoa a partir de sua idade e do ano atual
idade = int(input('Informe a sua idade: '))
ano_atual = int(input('Informe o ano atual: '))
niver = str(input('Você já fez aniversário essa ano? sim ou não: '))
if niver == 'sim':
    print(f'Você nasceu em {ano_atual - idade}')

else:
    print(f'Você nasceu em {ano_atual - idade - 1}')
