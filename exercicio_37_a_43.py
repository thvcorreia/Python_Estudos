"""
Exercícios da seção 4, questões de 37 a 43
"""
# 37. Leia o valor de um produto e imprima o valor com desconto de 12%
produto = float(input('Digite o valor do produto: \n'))
desconto = produto * 0.12
print(f'O preço do produto com desconto é: {round(produto - desconto, 2)}')


# 38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário com aumento de 25%
aumento = 0.25
salario = float(input('Informe o salário do funcionário: '))
print(f'O novo salário com aumento é: {round(salario + salario * aumento, 2)}')


# 39. A importância de R$ 780.000,00 será dividida entre 3 ganhadores de um concurso.
"""
A importância de R$ 780.000,00 será dividida entre 3 ganhadores de um concurso.
Sendo que da quantia total:
    1 - O primeiro ganhador receberá 46%
    2 - O segundo receberá 32%
    3 - O terceiro receberá o restante
Calcule e imprima a quantia ganha por cada um dos ganhadores
"""
premio = 780000.00
print(f'Os ganhadores do premio de R$ 780.000,00 do consurso receberão os seguintes valores')
print(f'1º colocado - R$ {premio * 0.46}')
print(f'2º colocado - R$ {premio * 0.32}')
print(f'3º colocado - R$ {premio * 0.22}')


# 40. Uma empresa contrata um encanador a R$ 30,00 por dia
"""
Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda
"""
imposto = 0.08
diaria = 30.00
dias = int(input('Informe a quantidade de dias trabalhados: \n'))
print(f'Líquido a receber é: {dias * diaria - dias * diaria * imposto}')


# 41. Faça um programa que leia o valor da hora de trabalho em reais.
"""
Leia as horas trabalhadas e o valor da hora de trabalho do mês, imprima o valor a ser pago ao funcionário, adicionando
10% sobre o valor calculado
"""
v_hora = float(input('Digite o valor da hora trabalhada: \n'))
hora = float(input('Digite a quantidade de horas trabalhadas: \n'))
adicional = v_hora * hora * 0.1
print(f'O valor a ser pago para o funcionário é: R$ {v_hora * hora + adicional}')


# 42. Receba o salário-base de um funcionário.
"""
Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base.
Além disso, ele paga 7% de imposto sobre o salário-base.
"""
salario = float(input('Informe o salário-base do funcionário: \n'))
gratificacao = salario * 0.05
imposto = salario * 0.07
print(f'Gratificação: {gratificacao}')
print(f'Imposto: {round(imposto, 2)}')
print(f'O salário a ser recebido: {salario + gratificacao - imposto}')


# 43. Escreva um programa de ajuda para vendedores.
"""
A partir de um valor total lido, mostre:
    1 - O total a pagar com desconto de 10%
    2 - O valor de cada parcela, no parcelamento de 3x sem juros
    3 - A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
    4 - A comissão do vendedor, no caso de venda parcelada (5% sobre o valor total)
"""
valor = float(input('Qual o valor total da compra: \n'))
desconto = valor * 0.1
print(f'Valor a vista com 10% de desconto: {valor - desconto} \n')
print(f'Valor parcelado em 3x - 1 de 3: {valor / 3}')
print(f'Valor parcelado em 3x - 2 de 3: {valor / 3}')
print(f'Valor parcelado em 3x - 3 de 3: {valor / 3} \n')
print(f'Comsissão para venda a vista: {round((valor - desconto) * 0.05, 2)} \n')
print(f'Comissão venda parcelada: {round(valor * 0.05, 2)}')
