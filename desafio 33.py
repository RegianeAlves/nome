n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
if n1 > n2:
    if n1 > n3:
        print('é o maior:{}'.format(n1))
    else:
        print('é o maior {}'.format(n3))

    if n2 < n3:
        print('é o menor {}'.format(n2))
    else:
        print('é o menor {}'.format(n3))
else:
    if n2 > n3:
        print('é o maior {}'.format(n2))
    else:
        print('é o maior {}'.format(n3))
    if n1 < n3:
        print('é o menor {}'.format(n1))
    else:
        print('é o menor {}'.format(n3))



