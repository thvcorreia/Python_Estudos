"""
Exercícios da seção 4, questões de 18 a 21
"""
# 18. Leia um valor de volume em metro cúbicos m³ e apresente-o convertido em litros
m = float(input('Digite o volume em m³ '))
print(f'O volume em litros é {1000 * m} L')


# 19. Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³
l = float(input('Digite o volume em litros '))
print(f'O volume em metros cúbicos é {l / 1000} m³')


# 20. Leia um valor de massa em quilogramas e apresente-o convertido em libras.
k = float(input('Digite o valor da massa em quilos, somente números '))
print(f'A massa em libras é {k / 0.45}')


# 21. Leia um valor de massa em libras e apresente-o convertido em quilogramas.
l = float(input('Digite a valor da massa em libras, ,somente números '))
print(f'A massa em quilogramas é {l * 0.45}Kg')


# 22. Leia um valor de comprimento em jardas e apresente-o convertido em metros
j = float(input('Digite o valor do comprimento em jardas '))
print(f'O comprimento em metros é {0.91 * j}')


# 23. Leia um valor de comprimento em metros e apresente-o convertido em jardas
m = float(input('Digite o valor do comprimento em metros '))
print(f'O comprimento em jardas é {m / 0.91}')
