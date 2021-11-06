from random import randint

lista = []


def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 9)
        lista.append(n)
        print(n, end=' ')
    print('PRONTO!')


def somapar():
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}  ')


sorteia()
somapar()