"""
Exercícios da seção 5, questões de 36 a 41
"""

# 36. Dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor.
"""
Maior ou igual a R$ 100.000,00 - R$ 700,00 + 16% das vendas
Menor que R$ 100.000,00 e maior ou igual a 80.000,00 - 650 + 14% das vendas
Menor que R$ 80.000,00 e maior ou igual a 60.000,00 - 600 + 14% das vendas
Menor que R$ 60.000,00 e maior ou igual a 40.000,00 - 550 + 14% das vendas
Menor que R$ 40.000,00 e maior ou igual a 20.000,00 - 500 + 14% das vendas
Menor que 20.000,00 - 400 + 14% das vendas
"""
vendedor = input('Vendedor: ')
valor_venda = float(input('Vendas: R$ '))
if valor_venda >= 100_000.00:
    comissao = 700 + valor_venda * 0.16
    print(f'Comissão: R$ {comissao}')
elif 80_000.00 <= valor_venda < 100_000.00:
    comissao = 650 + valor_venda * 0.14
    print(f'Comissão: R$ {comissao}')
elif 60_000.00 <= valor_venda < 80_000.00:
    comissao = 600 + valor_venda * 0.14
    print(f'Comissão: R$ {comissao}')
elif 40_000.00 <= valor_venda < 60_000.00:
    comissao = 550 + valor_venda * 0.14
    print(f'Comissão: R$ {comissao}')
elif 20_000.00 <= valor_venda < 40_000.00:
    comissao = 500 + valor_venda * 0.14
    print(f'Comissão: R$ {comissao}')
elif valor_venda < 20_000.00:
    comissao = 400 + valor_venda * 0.14
    print(f'Comissão: R$ {comissao}')
else:
    print('Verifique o valor informado')


# 37. As tarifas de certo parque de estacionamento são as seguintes:
"""
1ª e 2ª hora - R$ 1,00 cada
3ª e 4ª hora - R$ 1,40 cada
5ª hora e seguintes - R$ 2,00 cada
O numero de horas é sempre arredondado por excesso, deste modo quem estacionar por 61 minutos pagará por 120 minutos.
Os momentos de chegada e saída são apresentados na forma de pares inteiros. 12 50 (12:50)
Leia os momentos de chegada e partida e mostre o preço a ser cobrado.
Os momentos de chegada e de partida não são superiores a 24 horas.
Se passar de 24 horas, não é um erro e sim que a partida foi no dia seguinte ao da chegada.
"""
print('Parque de Estacionamento')
print('Tabela de preços\n1ª e 2ª hora - R$ 1,00 cada\n3ª e 4ª hora - R$ 1,40 cada\n5ª hora e seguintes - R$ 2,00 cada'
      '\nCaso exceda a hora será cobrada mais 1 hora')
hora_c = int(input('Hora de chegada: '))
minutos_c = int(input('Minuto de chegada: '))
hora_s = int(input('Hora de saída: '))
minutos_s = int(input('Minuto de saída: '))
tempo_permanencia = (hora_s * 60 + minutos_s) - (hora_c * 60 - minutos_c)
hora_permanencia = (tempo_permanencia / 60)
print(f'Hora de chegada às: {hora_c} {minutos_c}')
print(f'Hora de saída às: {hora_s} {minutos_s}')
print(f'Tempo de permanência: {tempo_permanencia}')
if tempo_permanencia <= 60:
    estacionamento = 1
    print(f'Estacionamento: R$ {estacionamento}')
elif (tempo_permanencia > 60) and (tempo_permanencia <= 120):
    estacionamento = 2
    print(f'Estacionamento: R$ {estacionamento}')
elif (tempo_permanencia > 120) and (tempo_permanencia <= 180):
    estacionamento = 2 + 1.4
    print(f'Estacionamento: R$ {estacionamento}')
elif (tempo_permanencia > 180) and (tempo_permanencia <= 240):
    estacionamento = 2 + 2.8
    print(f'Estacionamento: R$ {estacionamento}')
elif tempo_permanencia > 240:
    x = 0
    if (tempo_permanencia - 240) % 60 == 0:
        x = (tempo_permanencia - 240) / 60
        estacionamento = 2 + 2.8 + 2 * x
        print(x)
        print(f'Estacionamento: R$ {estacionamento}')
    else:
        x = (tempo_permanencia - 240) / 60
        # Usando int(x) em uma divisão, retorno somente a parte inteira dela
        y = int(x) + 1
        estacionamento = 2 + 2.8 + 2 * y
        print(y)
        print(f'Estacionamento: R$ {estacionamento}')


# 38. Leia uma data de nascimento fornecida por 3 números inteiros, Dia, Mês, Ano
"""
Teste a validade desta data de nascimento para saber se é válida
Teste se o dia é válido - dia > 0, dia <= 28 ou 29 para fevereiro - <= 30 e <= 31 dos outros meses
Teste a validade do mês > 0, < 13.
Teste a validade do ano: ano <= ano atual (use uma constante com valor igual a 2008)
Imprima data válida ou data inválida
"""
data = input('Verificando se uma data é válida - dia/mês/ano: ')
dia, mes, ano = data.split('/')
ano_atual = 2008
valida = False
if (0 < int(mes) < 13) and (int(dia) > 0) and (int(ano) <= ano_atual):
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
        else:
            valida = False
else:
    valida = False
if valida:
    print('\nData Válida')
else:
    print('\nData Inválida')


# 39. Dar aumento para os funcionários de acordo com uma tabela de salário atual e tempo de serviço
"""
Os funcionários com menor salário terão um aumento proporcionalmente maior que os com salários maior
Confirme o tempo de serviço na empresa
Cada um receberá um bônus adicional de salário
Leia o valor do salário atual
Lei o tempo de serviço na empresa (Número de anos de trabalho)
Calcule o salário reajustado e imprima o novo valor
Caso ele não tenha direito ao o aumento, imprima a msg informando.

ate 500,00             25%              abaixo de 1 ano         sem bônus
ate 1000,00            20%              de 1 a 3 anos           100,00
até 1500,00            15%              de 4 a 6 anos           200,00
até 2000,00            10%              de 7 a 10 amos          300,00
acima de 2000,00       Sem reajuste     mais de 10 anos         500,00
"""
print("""
Salário Atual       Reasjuste %      Tempo de Serviço          Bônus
ate 500,00             25%              abaixo de 1 ano         sem bônus
ate 1000,00            20%              de 1 a 3 anos           100,00
até 1500,00            15%              de 4 a 6 anos           200,00
até 2000,00            10%              de 7 a 10 amos          300,00
acima de 2000,00       Sem reajuste     mais de 10 anos         500,00
""")
funcionario = input('Funcionário: ')
if funcionario.isalpha():
    salario = float(input('Salário atual: '))
    tempo_servico = int(input('Tempo de serviço: '))
    if (salario <= 500) and (tempo_servico < 1):
        salario_novo = salario * 1.25
        print(f'{funcionario} - Novo salário: R$ {salario_novo:.2f}, sem direito ao Bônus')
    elif (salario <= 1000) and (1 <= tempo_servico <= 3):
        salario_novo = salario * 1.2 + 100
        print(f'{funcionario} - Novo salário: R$ {salario_novo:.2f}, já com Bônus de R$ 100,00')
    elif (salario <= 1500) and (4 <= tempo_servico < 6):
        salario_novo = salario * 1.15 + 200
        print(f'{funcionario} - Novo salário: R$ {salario_novo:.2f}, já com Bônus de R$ 200,00')
    elif (salario <= 2000) and (7 <= tempo_servico <= 10):
        salario_novo = salario * 1.10 + 300
        print(f'{funcionario} - Novo salário: R$ {salario_novo:.2f}, já com Bônus de R$ 300,00')
    elif (salario > 2000) and (tempo_servico > 10):
        salario_novo = salario + 500
        print('Não tem direito ao Reajuste')
        print(f'{funcionario} - Novo salário: R$ {salario_novo:.2f}, já com Bônus de R$ 500,00')
    else:
        print('Revise os dados informados')
else:
    print('Nome de funcionário inálido')


# 40. O custo de um carro novo...
"""
É a soma do custo de fábrica, da comissão do distribuidor e dos impostos.
A comissão e os impostos são calculados sobre o custo de fábrica
Leia o custo de fábrica e escreva o custo ao consumidor
Custo de fábrica            % do distribuidor       % dos impostos
até 12.000,00                       5                   isento
entre 12.000,00 e 25.000,00         10                    15
acima de 25.000,00                  15                    20
"""
custo = float(input('Custo de fábrica: '))
distribuidor = [custo * 0.05, custo * 0.1, custo * 0.15]
impostos = [custo * 0, custo * 0.15, custo * 0.20]
if custo <= 12000:
    n = 0
    carro_novo = custo + distribuidor[n] + impostos[n]
    print(f'O custo do carro novo: R$ {carro_novo:.2f}')
    print(f'Custo distribuidor: R$ {distribuidor[n]:.2f}')
    print(f'Impostos: R$ {impostos[n]:.2f}')
elif 12000 < custo <= 25000:
    n = 1
    carro_novo = custo + distribuidor[n] + impostos[n]
    print(f'O custo do carro novo: R$ {carro_novo:.2f}')
    print(f'Custo distribuidor: R$ {distribuidor[n]:.2f}')
    print(f'Impostos: R$ {impostos[n]:.2f}')
elif custo > 25000:
    n = 2
    carro_novo = custo + distribuidor[n] + impostos[n]
    print(f'O custo do carro novo: R$ {carro_novo:.2f}')
    print(f'Custo distribuidor: R$ {distribuidor[n]:.2f}')
    print(f'Impostos: R$ {impostos[n]:.2f}')
else:
    print('Revise os dados')
"""
Outra forma de fazer o programa acima

custo = float(input('Custo de fábrica: '))
distribuidor = [custo * 0.05, custo * 0.1, custo * 0.15]
impostos = [custo * 0, custo * 0.15, custo * 0.20]
if custo > 0:
    if custo <= 12000:
        n = 0
    elif 12000 < custo <= 25000:
        n = 1
    elif custo > 25000:
        n = 2
    else:
        print('')
else:
    print('Revise os dados')
carro_novo = custo + distribuidor[n] + impostos[n]
print(f'O custo do carro novo: R$ {carro_novo:.2f}')
print(f'Custo distribuidor: R$ {distribuidor[n]:.2f}')
print(f'Impostos: R$ {impostos[n]:.2f}')
"""

# 41. Faça um algorítmo que calcule o IMC de uma pessoa e mostre sua classificação.
"""
   IMC               Classificação
< 18,5              Abaixo do Peso
18,6 - 24,9            Saudável
25,0 - 29,9         Peso em Excesso
30,0 - 34,9         Obesidade Grau I
35,0 - 39,9         Obesidade Grau II (severa)
>= 40,0             Obesidade Grau II (mórbida)
"""
peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = round(peso / (altura ** 2), 1)
if imc > 0:
    if imc <= 18.5:
        print(f'{imc:.1f} - Abaixo do peso')
    elif 18.6 <= imc <= 24.9:
        print(f'{imc:.1f} - Saudável')
    elif 25.0 <= imc <= 29.9:
        print(f'{imc:.1f} - Peso em Excesso')
    elif 30.0 <= imc <= 34.9:
        print(f'{imc:.1f} - Obesidade Grau I')
    elif 35.0 <= imc <= 39.9:
        print(f'{imc:.1f} - Obesidade Grau II (severa)')
    elif imc >= 40.0:
        print(f'{imc:.1f} - Obesidade Grau III (mórbida)')
else:
    print('Verifique os dados informados')
