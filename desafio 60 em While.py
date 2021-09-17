num = int(input('Digite um número: '))
cont = 1
cont2 = 1
while cont <= num:
    cont2 *= cont
    cont += 1
print('Seu fatorial é {}'.format(cont2))