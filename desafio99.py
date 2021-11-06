from time import sleep


def maior(*num):
    cont = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        cont += 1
    print(f'foram informados {cont} valores ao todo')
    if cont == 0:
        print(f'O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(num)}.')
    prt()
    sleep(1)


def prt():
    print('-=' * 25)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()



