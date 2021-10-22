import time
from random import randint

numeros = []
dados = []

jogos = int(input('Quantos jogos você quer que eu sorteie: '))

for v in range(0, jogos):
    for c in range(0, 6):
        pc = randint(1, 61)
        if pc not in dados:
            dados.append(pc)
        else:
            while pc in dados:
                pc = randint(1, 61)
            dados.append(pc)
    dados.sort()
    numeros.append(dados[:])
    dados.clear()

for v in range(0, jogos):
    time.sleep(1)
    print(f'Jogo {v + 1}: {numeros[v]}')
