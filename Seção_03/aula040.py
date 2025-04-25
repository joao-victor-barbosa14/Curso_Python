"""
Calculadora com while
"""

while True:
    numero_01 = int(input('Escolha um número: '))
    numero_02 = int(input('Escolha outro número: '))
    expre_aritca = input('Escolha um operador: ')
    
    if expre_aritca == '+':
        soma01 = (numero_01 + numero_02)
        print(f'A soma dos números é {soma01}')
    elif expre_aritca == '-':
        soma02 = (numero_01 - numero_02)
        print(f'A subtração dos números é {soma02}')
    elif expre_aritca == '*':
        soma03 = (numero_01 * numero_02)
        print(f'A multiplicação dos números é {soma03}')
    elif expre_aritca == '/':
        soma04 = (numero_01 / numero_02)
        print(f'A divisão dos números é {soma04}')
    else:
        print('Verifique se o que você digitou está correto')
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
