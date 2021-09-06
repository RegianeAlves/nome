d = int(input('Dias alugados: '))
k = float(input('km rodados: '))
c = d * 60
c2 = k * 0.15
c3 = c + c2
print('O total a pagar é: R${:.2f}'.format(c3))