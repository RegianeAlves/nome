from math import hypot
n = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
c = hypot(n, n2)
print('o comprimento da hypotenusa é {:.2f}'.format(c))
