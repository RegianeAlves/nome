n = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n == n2:
    print('Não existe valor maior,os dois são iguais {},{}'.format(n, n2))
elif n > n2:
    print('{} é o maior'.format(n))
else:
    print('{} é o maior'.format(n2))
