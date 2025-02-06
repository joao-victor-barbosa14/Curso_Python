"""
Exercício
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

print(f'Seu nome é {nome}')
print(f'Seu nome invertido é {nome[::-1]}')
print(f'Seu nome tem {len(nome)} letras')
print(f'A primeira letra do seu nome é {nome[1]}')
print(f'A última letra do seu nome é {nome[-1]}')

if nome and idade == '':
    print('Desculpe, você deixou algum campo vazio')
