"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira 
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 8:
        print('Oito não está aqui')
        continue
    if contador == 40:
        print('Quarenta não está aqui')
        continue
    if contador == 30:
        print('Trinta não está aqui')
    
    print(contador)

    if contador == 50:
        break


print('Acabou')
    
