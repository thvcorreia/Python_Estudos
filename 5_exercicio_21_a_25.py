"""
Exercícios da seção 5, questões de 21 a 25
"""
import math

# 21. Escreva um menu. Leia as opções e execute a operação escolhida, escreva uma msg de erro se a opção fo inválida
"""
Escolha a opção:
1 - Soma de 2 números.
2 - Diferença entre dois números. (Maior pelo menor).
3 - Produto entre dois números.
4 - Divisão entre 2 números (Denominador não pode ser zero).
Opção
"""
print('1 - Soma de 2 números.\n2 - Diferença entre dois números. (Maior pelo menor).\n3 - Produto enrte dois números.'
      '\n4 - Divisão entre 2 números (Denominador não pode ser zero).')
n = int(input('Opção: '))
if n > 4 or n < 1:
    print('Opção inexistente')
else:
    numero1 = float(input('Informe um número: '))
    numero2 = float(input('Informe outro: '))
    if n == 1:
        print(f'A soma = {numero1 + numero2}')
    elif n == 2:
        if numero1 > numero2:
            print(f'A subtração = {numero1 - numero2}')
        else:
            print(f'A subtração = {numero2 - numero1}')
    elif n == 3:
        print(f'A Multiplicação = {numero1 * numero2}')
    else:
        if numero2 == 0:
            print('Erro! Denominador não pode ser zero')
        else:
            print(f'A Divisão = {numero1 / numero2:.2f}')


# 22. Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
"""
As condições são:
1 - Ter pelo menos 65 anos.
2 - Ou ter trabalhado por pelo menos 30 anos
3 - Ou ter pelo menos 60 e ter trabalhado por pelo menos 25 anos
"""
idade = int(input('Informe a idade do trabalhador: '))
tempo = float(input('Informe o tempo de serviço: '))
if (idade == 65) or (tempo == 30) or (idade == 60 and tempo == 25):
    print(f'\nEle pode se aposentar!')
else:
    print(f'\nNão pode se aposentar!')


# 23. Determine se um determinado ano lido é bissexto.
"""
Um ano é bissexto se for divisível por 400 ou se for divisível por 4.
E não for divisível por 100
"""
ano = int(input('Informe o ano: '))
if (ano % 400 == 0) or (ano % 4 == 0) and (ano % 100 != 0):
    print('Ano bissexto')
else:
    print('Ano não bissexto')


# 24. Uma empresa vende o mesmo produto para 4 diferentes estados.
"""
Cada estado possui uma taxa diferente de imposto sobre o produto (MG - 7%, SP - 12%, RJ - 15% e MS - 8%.
Usuário entra com o valor e o estado de destino.
O programa retorna o preço final do produto com imposto
Se o estado digitado não for válido, mostrar uma msg de erro.
"""
produto = float(input('informe o valor do produto: '))
print('\n1 - MG 7% \n2 - SP 12% \n3 - RJ 15% \n4 - MS 8% ')
estado = ['MG', 'SP', 'RJ', 'MS']
imposto = ['0.07', '0.12', '0.15', '0.08']
n = int(input('Informe o estado de destino: '))
print(f'O preço final do produto para {estado[n - 1]} é {produto + (produto * float(imposto[n - 1]))}')


# 25. Calcule as raízes da equação do 2º grau.
"""
A variável a tem que ser diferente de zero. Caso seja igual, imprima uma msg - Não é uma equação do 2º grau
Se delta < 0, não existe real. Imprima a msg - Não existe raiz
Se delta = 0, existe uma raiza real. Imprima a raiz e a msg - Raiz única
se delta > 0, imprima as duas raizes reais.
ax² + bx + c = 0
x = -b +- raiz delta / 2a
delta = b² - 4ac
"""
print('ax² + bx + c = 0')
a = float(input('Informe o valor de a: '))
if a == 0:
    print('Não é uma equação do 2º Grau')
else:
    b = float(input('Informe o valor de b: '))
    c = float(input('Informe o valor de c: '))
    delta = b ** 2 - 4 * (a * c)
    if delta < 0:
        print('Não existe raiz')
    else:
        x1 = (- b + float(math.sqrt(delta))) / 2 * a
        x2 = (- b - float(math.sqrt(delta))) / 2 * a
        if delta == 0:
            print(f'x = {x1:.2f} - Raiz única')
        else:
            print(f'x = {x1:.2f}, x = {x2:.2f}')
