from time import sleep


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
            sleep(0.5)
    else:
        if passo > 0:
            passo = passo * -1
        for c in range(inicio, fim - 1, passo):
            print(c, end=' ')
            sleep(0.5)
    print('FIM')
    print('-' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-' * 30)
contador(inicio, fim, passo)
