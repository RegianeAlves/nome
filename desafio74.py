from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
#tupla2 = tuple(randint(0, 10) for c in range(0, 5))
print(f'Os valores sorteados foram {tupla}')
#print(f'Os valores sorteados foram {tupla2}')
maior = menor = 0
for c in range(0, 5):
    if c == 0:
        maior = tupla[c]
        menor = tupla[c]
    else:
        if tupla[c] > maior:
            maior = tupla[c]
        elif tupla[c] < menor:
            menor = tupla[c]
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
