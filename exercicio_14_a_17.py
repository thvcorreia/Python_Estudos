"""
Exercícios da seção 4, questões de 14 a 17
"""
pi = 3.14    # Para as questões 14 e 15


# 14. Leia um ângulo em graus e apresente-o convertido em radianos.
g = float(input('Digite quantos graus tem o ângulo, somente números '))
print(f'O ângulo informado tem {g * pi / 180} radianos')


# 15. Leia um ângulo em radianos e apresente-o convertido em graus.
r = float(input('Digite quantos radianos tem o ângulo '))
print(f'O ângulo informado tem {r * 180 / pi}º')     # Para simplificar


# 16. Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros
p = float(input('Digite o valor do comprimento em polegadas, somente números '))
print(f'O comprimento em centímetros é {p * 2.54} cm')


# 17. Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas
c = float(input('Digite o valor do comprimento em centímentros, somente números '))
print(f'O comprimento em polegadas é {c / 2.54}"')
