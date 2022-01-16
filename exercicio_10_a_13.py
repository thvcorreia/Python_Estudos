"""
Exercícios da seção 4, questões de 10 a 13
"""
# 10. Leia uma velocidade em km/h e apresente-a convertida em m/s.
K = float(input('Digite a velocidade em quiilometros por hora, km/h '))
M = K/3.6
print(f'Sua velocidade em m/s é {M}')


# 11. Leia uma velocidade em m/s e apresente-a convertida em km/h.
M = float(input('Digite a velocidade em metros por segundo, m/s '))
K = M * 3.6
print(f'Sua velocidade em km/h é {K}')


# 12. Leia uma distância em milhas e apresente-a convertida em quilômetros.
M = float(input('Digite a distância em milhas '))
K = M * 1.61
print(f'A distância em quilometros é {K}')


# 13. Leia uma distância em quilômetros e apresente-a convertida em milhas.
K = float(input('Digite a distância em quilômetros '))
M = K / 1.61
print(f'A distância em milhas é {M}')
