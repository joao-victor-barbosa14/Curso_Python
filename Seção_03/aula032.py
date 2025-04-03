"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero01 = input('Digite um número: ')
parouimpar = (numero01 % 2)

if parouimpar == '0':
    print('Esse número é par')
elif parouimpar == '1':
    print('Esse número é impar')
else:
    ('Esse número não é inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = int(input('Que horas são? '))

if horario <= 11:
    print('Bom dia')
elif horario <= 17:
    print('Boa tarde')
else:
    print('Boa noite')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal'; maior que 6 escreva "Seu nome é muito grande". 
"""
name = input('Qual é seu nome? ')
name = len(name)

if name <= 4:
    print('Seu nome é curto!')
elif name <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é grande!')
