n = int(input('Digite a Velocidade: '))
if n>80:
    s = n - 80
    m = s * 7
    print('Multado!')
    print('Valor: R${}'.format(m))
