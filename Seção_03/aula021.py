"""
Operadores lógicos 
and (e)  or (ou) nor (não)
and - Todas as condições precisam ser
verdadeiras.
Se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor
São considerados falsy (que você já viu)
0 0.0 '' False
Também existe o tipo None que é
usando para representar um não valor
"""
entrada = input('[E]entrar [S]sair: ')
senha_digitada = input('Senha: ')

if entrada == 'E' and senha_digitada == 'Jv2010':
    print('Você entrou...')
else:
    ('Saindo...')
