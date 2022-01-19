"""
Exercícios da seção 5, questões de 6 a 10
"""
# 6. Faça um programa que receba dois números e mostre qual o maior e mostre qual a diferença entre eles
# x, y = int(input('Informe os dois numeros: ').split(" "))
x = int(input('Informe o primeiro número: '))
y = int(input('Informe o segundo número: '))
if x > y:
    print(f'{x} é o maior')
    print(f'A diferença entre eles é {x - y}')
elif x == y:
    print('Números iguais')
else:
    print(f'{y} é o maior')
    print(f'A diferença entre eles é {y - x}')


# 7. Faça um programa que receba dois números e mostre qual o maior, se forem iguais, mostre números iguais.
# a, b = input('Informe os dois numeros: ').split(" ")
a = input('Informe o primeiro número: ')
b = input('Informe o segundo número: ')
if a > b:
    print(f'{a} é o maior')
elif a == b:
    print('Números iguais')
else:
    print(f'{b} é o maior')


# 8. Leia duas notas de um aluno, verifique se as notas são válidas e imprima a média delas.
"""
1 - Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0
2 - Caso a nota não possua um valor válido, esse fato deve ser mostrado ao usuário e o programa termina.
"""
aluno = input('Informe o nome do aluno: ')
if aluno.isalpha():
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    if (nota1 or nota2) > 10 or (nota1 or nota2) < 0:
        print('Nota inválida!')
        exit()
    else:
        print(f'Média: {round((nota1 + nota2) / 2, 0)}')
else:
    print('Digite um nome válido')


# 9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
"""
1 - Se a prestação for maior que 20% do salário, imprima - Empréstimo não concedido
2 - Se não, imprima - Empréstimo concedido
"""
salario = float(input('Informe o salário: '))
prestacao = float(input('Informe o valor da prestação: '))
if prestacao > salario * 0.2:
    print('Empréstimo não concedido!')
    print('Prestação superior a 20% do salário')
else:
    print('Empréstimo concedido!')


# 10. Leia a altura e o sexo de uma pessoa e calcule o seu peso ideal.
sexo = input('Informe seu sexo, F = Femenino ou M = Masculino: ')
h = float(input('Informe a sua altura: '))
if sexo == 'F':
    print(f'Seu peso ideal é: {(62.1 * h) - 44.7:.2f}')    # Posso arredondar assim
else:
    print(f'Seu peso ideal é: {round((72.7 * h) - 58,2)}')    # Ou arredondar assim
