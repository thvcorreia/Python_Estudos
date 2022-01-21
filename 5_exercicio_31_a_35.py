"""
Exercícios da seção 5, questões de 31 a 35
"""
# 31. Leia a altura e peso de uma pessoa, verifique e mostre qual a classificação dessa pessoa
"""
Menor que 1,20, peso até 60 kg - A, entre 60 e 90 - D, acima de 90 - G
De 1,20 a 1,70, peso até 60 kg - B, entre 60 e 90 - E, acima de 90 - H
Maior que 1,70, peso até 60 kg - C, entre 60 e 90 - F, acima de 90 - I
"""
print('Classificar uma pessoa pela altura e peso')
altura = float(input('Altura: '))
peso = float(input('Peso: '))
if altura < 1.20:
    if peso <= 60:
        print('Classificação: A')
    elif 60 < peso <= 90:
        print('Classificação: D')
    else:
        print('Classificação: G')
elif 1.20 < altura <= 1.70:
    if peso <= 60:
        print('Classificação: B')
    elif 60 < peso <= 90:
        print('Classificação: E')
    else:
        print('Classificação: H')
else:
    if peso <= 60:
        print('Classificação: C')
    elif 60 < peso <= 90:
        print('Classificação: F')
    else:
        print('Classificação: I')


# 32. Leia o código de um produto do cardápio e a quantidade.
"""
O programa deve calcular o valor a ser pago
Cada execução será calculado somente um pedido.
Produto         - Código - preço
Cachorro quente - 100    - 1.20
Bauru simples   - 101    - 1.30
Bauru com ovo   - 102    - 1.50
Hanburger       - 103    - 1.20
Cheeseburger    - 104    - 1.70
Suco            - 105    - 2.20
Refrigerante    - 106    - 1.00
"""
print("""
Produto         - Código - preço
Cachorro quente - 100    - 1.20
Bauru simples   - 101    - 1.30
Bauru com ovo   - 102    - 1.50
Hanburger       - 103    - 1.20
Cheeseburger    - 104    - 1.70
Suco            - 105    - 2.20
Refrigerante    - 106    - 1.00
""")
produto = ['Cachorro quente', 'Bauru simples', 'Bauru com ovo', 'Hanburger', 'Cheeseburger', 'Suco', 'Refrigerante']
codigo = [100, 101, 102, 103, 104, 105, 106]
preco = [1.20, 1.30, 1.50, 1.20, 1.70, 2.20, 1.00]
cod_produto = int(input('Código do produto: '))
n = cod_produto - 100
if (cod_produto < 100) or (cod_produto > 106):
    print('Código inválido')
else:
    quantidade = int(input('Informe a quantidade: '))
    print(f'Foi solicitado {quantidade} - {produto[n]} a R$ {preco[n]}')
    print(f'Valor a pagar: {quantidade * preco[n]}')


# 33. Um produto vai sofrer aumento de acordo com a tabela abaixo
"""
Leia o preço antigo, calcule e escreva o preço novo
Escreva uma msg em função do preço novo.
Preço antigo          percentual de aumento          Preço novo                  Mensagem
até R$ 50                       5%                até R$ 80                      Barato
entre R$ 50 e R$ 100            10%               entre R$ 80 e R$ 120           Normal
acima de R$ 100                 15%               entre R$ 120 e R$ 200          Caro
                                                  acima de R$ 200                Muito caro
"""
preco_antigo = float(input('Preço antigo: R$ '))
if preco_antigo <= 50:
    preco_novo = preco_antigo * 1.05
    print(f'{preco_novo:.2f}')
elif (preco_antigo > 50) and (preco_antigo <= 100):
    preco_novo = preco_antigo * 1.1
    print(f'{preco_novo:.2f}')
else:
    preco_novo = preco_antigo * 1.15
    print(f'{preco_novo:.2f}')
if preco_novo <= 80:
    print('Barato')
elif (preco_novo > 80) and (preco_novo <= 120):
    print('Normal')
elif (preco_novo > 120) and (preco_novo <= 200):
    print('Caro')
else:
    print('Muito Caro')


# 34. Leia a nota e o número de faltas de um aluno.
"""
Escreva seu conceito, quando um aluno tem mais de 20 falta, ocorre uma redução de conceito.
nota         conceito até 20 faltas   conceito mais de 20 faltas
9.0 até 10.0          A                           B
7.5 até 8.9           B                           C
5.0 até 7.4           C                           D
4.0 até 4.9           D                           E
0.0 até 3.9           E                           E 
"""
nome = str(input('Digite o nome do aluno: '))
nota = float(input('Nota: '))
faltas = int(input('Faltas: '))
if 9 <= nota <= 10:
    if faltas < 20:
        print('Conceito - A')
    else:
        print('Conceito - B')
elif 7.5 <= nota <= 8.9:
    if faltas < 20:
        print('Conceito - B')
    else:
        print('Conceito - C')
elif 5 <= nota <= 7.4:
    if faltas < 20:
        print('Conceito - C')
    else:
        print('Conceito - D')
elif 4 <= nota <= 4.9:
    if faltas < 20:
        print('Conceito - D')
    else:
        print('Conceito - E')
elif 0 <= nota <= 3.9:
    print('Conceito - E')
else:
    print('Algum valor errado, tente novamente!')

# 35. Leia uma data e determine se ela é válida.
"""
Verifique se o mês está entre 1 e 12
Se o dia existe naquele mês
Fevereiro tem 29 dias em anos bissextos e 28 em anos não bissextos
"""
data = input('Verificando se uma data é válida - dia/mês/ano: ')
dia, mes, ano = data.split('/')
valida = False
if int(mes) > 12 or int(dia) > 31:
    valida = False
else:
    if int(mes) == 2:
        if (int(ano) % 4 == 0) and (int(ano) % 100 != 0) and int(dia) <= 29:
            print('Ano bissexto')
            valida = True
        elif int(dia) <= 28:
            valida = True
        else:
            valida = False
    else:
        if int(mes) == 1 or int(mes) == 3 or int(mes) == 5 or int(mes) == 7 or int(mes) == 8 or int(mes) == 10 \
                or int(mes) == 12:
            if int(dia) <= 31:
                valida = True
            else:
                valida = False
        elif int(mes) == 4 or int(mes) == 6 or int(mes) == 9 or int(mes) == 11:
            if int(dia) <= 30:
                valida = True
            else:
                valida = False
if valida:
    print('\nData Válida')
else:
    print('\nData Inválida')
