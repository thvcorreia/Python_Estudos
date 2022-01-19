"""
Exercícios da seção 5, questões de 11 a 15
"""
import math

# 11. Leia um número inteiro maior que zero e devolva
"""
1 - A soma de todos os seus algarismos
2 - Se o número não for maior que zero, exiba Número inválido
"""
# a = int(input('Informe um número positivo maior que zero: '))
# if a > 0:
#    print(sum(int(i) for i in a))
# else:
#    print('Número inválido')

# 12. Leia um número inteiro
"""
1 - Se for negativo, Número inválido
2 - Se for positivo, calcular o logaritimo.
"""
b = int(input('Informe um númeor positivo maior que zero: '))
if b >= 0:
    print(f'O logarírimo é {math.log(b):.2f}')
else:
    print('Número inválido')


# 13. Calcule a média ponderada das notas de 3 provas.
"""
1 - A primeira e a segunda prova tem peso 1 e a terceira tem peso 2.
2 - Mostrar a media do aluno e mostrar se foi ou não aprovado
3 - A nota de aprovação deve ser igual ou superior a 60 pontos
"""
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))
media = (nota1 + nota2 + 2 * nota3) / 4
print(f'A média do aluno é: {media:.1f}')
if media >= 60:
    print('Aluno Aprovado')
else:
    print('Aluno Reprovado')


# 14. Calcule a nota final de um estudante a partir de 3 notas de 0 a 10, respectivamente:
"""
1 - Um trabalho de laboratório, peso 2
2 - Uma avaliação semestral, peso 3
3 - Um exame final, peso 5
4 - Média para ser reprovado - 0 a 2,9
5 - Média para recuperação - 3 a 4,9
6 - Aprovado
"""
aluno = input('Nome do aluno: ')
if aluno.isalpha():
    laboratorio = float(input('Nota trabalho de laboratório: '))
    avaliacao = float(input('Nota avaliação semestral: '))
    exame = float(input('Nota exame final: '))
    if 0 <= (laboratorio or avaliacao or exame) <= 10:
        media = (2 * laboratorio + 3 * avaliacao + 5 * exame) / 10
        print(f'A média do aluno é: {media:.1f}')
        if 0 <= media <= 2.9:
            print('Aluno Reprovado')
        elif 3 <= media <= 4.9:
            print('Aluno de Recuperação')
        else:
            print('Aluno Aprovado')
    else:
        print('Nota inválida')
else:
    print('Nome de aluno inválido')


# 15. Usando Switch, leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente.
"""
1 - Domingo
2 - Segunda
E assim por diante
"""
print("""1 - Domingo \n2 - Segunda \n3 - Terça \n4 - Quarta \n5 - Quinta \n6 - Sexta \n7 - Sábado""")
n = int(input('Escolha um número de 1 a 7: '))
if n == 1:
    print('Domingo')
elif n == 2:
    print('Sengunda')
elif n == 3:
    print('Terça')
elif n == 4:
    print('Quarta')
elif n == 5:
    print('Quinta')
elif n == 6:
    print('Sexta')
elif n == 7:
    print('Sábado')
else:
    print('Número fora do solicitado')
