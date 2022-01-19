"""
Exercícios da seção 5, questões de 26 a 30
"""
import random

# 26. Leia a distância em Km e a qunatidade de gasolina consumidos por um carro em percurso.
"""
Calcule o consumo em Km/l e escreva uma mensagem:
Consumo menor do que 8 - Venda o carro!
Entre 8 e 12 - Econômico!
maior que 12 - Super Econômico!
"""
km = float(input('Informe a distância percorriada em km: '))
combustivel = float(input('Informe a quantidade litros de combustível usada: '))
consumo = km / combustivel
if consumo < 8:
    print(f'{consumo:.2f}/l, Venda o carro')
elif 8 <= consumo <= 12:
    print(f'{consumo:.2f}/l, Econômico')
else:
    print(f'{consumo:.2f}/l, Super Econômico')


# 27. Dada a idade de um nadador, classifique-o em uma das categorias:
"""
Infantil A - 5 a 7
Infantil B - 8 a 10
Juvenil A - 11 a 13
Juvenil B - 14 a 17
Sênior - maior de 18 anos
"""
nome = input('Nome: ')
idade = int(input('Idade: '))
if 5 <= idade <= 7:
    print('Infantl A')
elif 8 <= idade <= 10:
    print('Infantil B')
elif 11 <= idade <= 13:
    print('Juvenil A')
elif 14 <= idade <= 17:
    print('Juvenil B')
elif idade > 17:
    print('Sênior')
else:
    print('Ainda não atingiu a idade mínima para participar da competição')


# 28 . Leia 3 números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo com o número digitado.
"""
1 - Geométrica - raiz cúbica de x * y * z
2 - Ponderada - (x + 2 * y +3 * z) / 6
3 - Harmônica - 1 / (1 / x + 1 / y + 1 / z)
4 - Aritmética - (x + y + z) / 3
"""
x = int(input('Primeiro número: '))
y = int(input('Segundo número: '))
z = int(input('Terceiro Número: '))
print("""1 - Geométrica - raiz cúbica de x * y * z
2 - Ponderada - (x + 2 * y +3 * z) / 6
3 - Harmônica - 1 / (1 / x + 1 / y + 1 / z)
4 - Aritmética - (x + y + z) / 3""")
opcoes = ['Média Geométrica', 'Média Ponderada', 'Média Harmônica', 'Média Aritimética']
matriz = [(x * y * z) ** (1 / 3), (x + 2 * y + 3 * z) / 6, 1 / (1 / x + 1 / y + 1 / z), (x + y + z) / 3]
n = int(input('Escolha a sua operação: '))
if 1 <= n <= 4:
    print(f'{str(opcoes[n - 1])}')
    print(f'{float(round(matriz[n - 1],2))}')
#   print(f'{float(cmath.cbtr(x * y * z))}')
else:
    print('Operação inválidade, escolha uma opção de 1 a 4')


# 29. Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores que 100.
"""
Escolha números aleatórios entre 1 e 100.
Mostre a pergunta na tela, qual a soma de a + b.
Peça a resposta
Faça cinco perguntas ao aluno.
Mostre a ele as perguntas e as respostas certas.
Mostre quantas ele acertou.
"""
print('Prova de matemática')
n = 0
a = random.randrange(1, 100)
b = random.randrange(1, 100)
print(f'Qual a soma de {a} + {b}')
resposta = int(input('Qual a sua resposta: '))
soma = a + b
print(f'A soma de {a} + {b} = {resposta}')
print(f'Sua resposta foi: {soma}')
if resposta == soma:
    print('Resposta Correta')
    n = n + 1
else:
    print('Resposta Errada')
a1 = random.randrange(1, 100)
b1 = random.randrange(1, 100)
print(f'\nQual a soma de {a1} + {b1}')
resposta1 = int(input('Qual a sua resposta: '))
soma1 = a1 + b1
print(f'A soma de {a1} + {b1} = {resposta1}')
print(f'Sua resposta foi: {soma1}')
if resposta1 == soma1:
    print('Resposta Correta')
    n = n + 1
else:
    print('Resposta Errada')
a2 = random.randrange(1, 100)
b2 = random.randrange(1, 100)
print(f'\nQual a soma de {a2} + {b2}')
resposta2 = int(input('Qual a sua resposta: '))
soma2 = a2 + b2
print(f'A soma de {a1} + {b1} = {resposta2}')
print(f'Sua resposta foi: {soma2}')
if resposta2 == soma2:
    print('Resposta Correta')
    n = n + 1
else:
    print('Resposta Errada')
a3 = random.randrange(1, 100)
b3 = random.randrange(1, 100)
print(f'\nQual a soma de {a3} + {b3}')
resposta3 = int(input('Qual a sua resposta: '))
soma3 = a3 + b3
print(f'A soma de {a3} + {b3} = {resposta3}')
print(f'Sua resposta foi: {soma3}')
if resposta3 == soma3:
    print('Resposta Correta')
    n = n + 1
else:
    print('Resposta Errada')
a4 = random.randrange(1, 100)
b4 = random.randrange(1, 100)
print(f'\nQual a soma de {a4} + {b4}')
resposta4 = int(input('Qual a sua resposta: '))
soma4 = a4 + b4
print(f'A soma de {a4} + {b4} = {resposta4}')
print(f'Sua resposta foi: {soma4}')
if resposta4 == soma4:
    print('Resposta Correta')
    n = n + 1
else:
    print('Resposta Errada')
print(f'\nVc acertou {n} questões!')


# 30. Leia 3 números e mostre-os em ordem crescente
print('Escolha os números')
a = float(input('Número 1: '))
b = float(input('Número 2: '))
c = float(input('Número 3: '))
print('Números em Ordem crescente')
matriz = [a, b, c]
ordem_crecente = sorted(matriz)
print(ordem_crecente)
