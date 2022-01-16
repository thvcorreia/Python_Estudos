comprimento = float(input('Informe o comprimento do terreno: '))
largura = float(input('informe a largura do terreno'))
tela = float(input('Informe o preço do metro da tela R$ '))
print(f'Para cercar todo o terreno será necessário R$ {(comprimento * 2 + largura * 2) * tela}')
