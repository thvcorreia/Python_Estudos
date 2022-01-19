"""
Exercícios da seção 5, questões de 16 a 20
"""
# 16. Leia um número inteiro entre 1 e 12 e imprima o mês correspondente a este número.
print("""Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, Dezembro""")
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
       'Dezembro']
n = int(input('Escolha um número de 1 a 12: '))
print(f'O mês escolhido foi: {mes[n - 1]}')


# 17. Calcule e mostre a área de um trapézio.
print('Área de um trapézio')
basemaior = float(input('Informe o tamanho da base maior do trapézio: '))
basemenor = float(input('Informe o tamanho da base menor do trapézio: '))
if (basemaior and basemenor) > 0:
    altura = float(input('Informe a altura do trapézio: '))
    area = ((basemaior + basemenor) * altura) / 2
    print(f'A área do trapézio é: {area:.2f}')
else:
    print('Nenhuma da bases podem ser igual ou menor que zero')


# 18. Mostre ao usuário um menu de 4 opções de operações matemáticas
"""
O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e então realiza a operação,
mostrando o resultado e saindo
"""
print('1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
n = int(input('Escolha a operação desejada: '))
numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe outro: '))
if n == 1:
    print('1 - Adição')
    print(f'A soma = {numero1 + numero2}')
    exit()
elif n == 2:
    print('2 - Subtração')
    print(f'A subtração = {numero1 - numero2}')
    exit()
elif n == 3:
    print('3 - Multiplicação')
    print(f'A Multiplicação = {numero1 * numero2}')
    exit()
elif n == 4:
    print('4 - Divisão')
    print(f'A Divisão = {numero1 / numero2}')
    exit()
else:
    print('Opção inexistente ')
    exit()


# 19. Verifique se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.
x = int(input('Informe um número inteiro: '))
if x >= 0:
    if x % 3 == 0 and x % 5 == 0:
        print('Número não pode ser verificado')
    elif x % 3 == 0:
        print('Divisível por 3')
    elif x % 5 == 0:
        print('Divisível por 5')
else:
    print('Número inválido')

# 20. Dado 3 valores, verificar se eles podem ser os lados de um triangulo e qual triangulo
"""
1 - O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados
2 - Equilátero - Tem os 3 lados iguais
3 - Isóscele - Tem o comprimento de 2 lados iguais
4 - Escaleno - Tem os 3 lados difrentes
"""
a = int(input('Informe um número inteiro: '))
b = int(input('Informe um número inteiro: '))
c = int(input('Informe um número inteiro: '))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Triângulo Equilátero')
    elif a == b or a == c or b == c:
        print('Triângulo Isoscele')
    elif a != b and a != c and b != c:
        print('Triângulo Escaleno')
else:
    print('Não é um Triângulo')
