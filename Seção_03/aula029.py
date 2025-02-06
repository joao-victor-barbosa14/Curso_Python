"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numeros = input('Vou somar mais um número que você digitar: ')

try: 
    numerof = float(numeros)
    print(f'A soma do número {numeros} é {numerof + 1:.0f}')
except:
    print('Isso não é um número')
