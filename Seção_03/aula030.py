"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro 
local_carro = 101 # local em que o carro está na estrada

Radar = 60 # velocidade máxima do radar 1
Local = 100 # local onde o radar 1 está
Radar_Range = 1 # A distância onde o radar pega

if velocidade > Radar:
    print('Você ultrapassou a velocidade do radar')

if local_carro >= (Local - Radar_Range) and local_carro <= (Local + Radar_Range):
    print('Carro multado em radar 1')
