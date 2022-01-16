"""
Exercícios da seção 4, questões de 6 a 9
"""
# 6. Leia uma temperatura em graus Celsius e apresente-a convertida em Fahrenheit.
C = float(input('Qual a temperatura em graus Celsius? '))
print(f'A temperatura em graus Celsius é {C}')
F = C * (9.0/5.0) + 32.0
print(f'Em Fahrenheit é {F} {C * (9.0/5.0) + 32.0}')


# 7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em Celsius.
F = float(input('Qual a temperatura em graus Fahrenheit? '))
print(f'A temperatura em graus Fahrenheit é {F}')
C = 5.0 * (F -32.0) / 9.0
print(f'Em Celsius é {C} {5.0 * (F -32.0) / 9.0}')


# 8. Leia uma temperatura em graus Kevin e apresente-a convertida em Celsius.
K = float(input('Qual a temperatura em graus Kevin? '))
print(f'A temperatura em graus Kevin é {K}')
C = K - 273.15
print(f'Em Celsius é {C} {K - 273.15}')


# 9. Leia uma temperatura em graus Celsius e apresente-a convertida em Kevin.
C = float(input('Qual a temperatura em graus Celsius? '))
print(f'A temperatura em graus Celsius é {C}')
K = C + 273.15
print(f'Em Kevin é {K} {C + 273.15}')
