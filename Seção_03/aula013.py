"""
Introdução f-strings
"""
nome = 'João Victor'
altura = 1.68
peso = 61
imc = peso / (altura * altura)
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
