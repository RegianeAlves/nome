num = int(input('Digite um número: '))
cont = 1
for c in range(1, num + 1):
    cont *= c
print('Seu fatorial é {}'.format(cont))