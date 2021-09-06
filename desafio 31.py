n = float(input('Digite a distância da viagem: '))
if n<=200:
    c = n * 0.50
    print('preço da passagem:{:.2f}'.format(c))
else:
    p = n * 0.45
    print('preço da passagem:{:.2f}'.format(p))