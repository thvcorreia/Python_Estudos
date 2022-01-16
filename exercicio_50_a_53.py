"""
Exercícios da seção 4, questões de 44 a 50
"""
import math

# 50. Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule a distância da origem
x = float(input('Informe a coordenada x: '))
y = float(input('Informe a coordenada y: '))
print(f'Com os coordenadas informadas temos uma distância igual a: {round(math.sqrt(x ** 2 + y ** 2), 2)}')


# 51. Três amigos joaram na loteria.
"""
Caso eles ganhem, o prêmio o deve ser repartido proporcionalmente ao valor que cada um deu para a realização da aposta.
Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio
com base no valor investido.
"""
premio = float(input('Qual o valor do Prêmio: '))
aposta1 = float(input('Ivestidor 1 - digite o valor investido na aposta: '))
aposta2 = float(input('Ivestidor 2 - digite o valor investido na aposta: '))
aposta3 = float(input('Ivestidor 3 - digite o valor investido na aposta: '))
soma = aposta1 + aposta2 + aposta3
porcentagem_aposta1 = round((aposta1 * 100) / soma,0)
porcentagem_aposta2 = round((aposta2 * 100) / soma,0)
porcentagem_aposta3 = round((aposta3 * 100) / soma,0)
print(f'Do prêmio de R$ {premio}, cada investidor receberá proporcionalmente:')
print(f'Ivestidor 1 tem direito a {porcentagem_aposta1}% do valor - {premio * porcentagem_aposta1 / 100}')
print(f'Ivestidor 2 tem direito a {porcentagem_aposta2}% do valor - {premio * porcentagem_aposta2 / 100}')
print(f'Ivestidor 3 tem direito a {porcentagem_aposta3}% do valor - {premio * porcentagem_aposta3 / 100}')


# 53. Leia as dimensões de um terreno, bem como o preço do metro de tela. Imprima o custa para a cercar o terreno
comprimento = float(input('Informe o comprimento do terreno: '))
largura = float(input('informe a largura do terreno'))
tela = float(input('Informe o preço do metro da tela R$ '))
print(f'Para cercar todo o terreno será necessário R$ {(comprimento * 2 + largura * 2) * tela}')
