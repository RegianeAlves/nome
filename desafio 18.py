import math
from math import cos, sin, tan
n = float(input('Digite um numero: '))
c = math.cos(math.radians(n))
c2 = math.sin(math.radians(n))
c3 = math.tan(math.radians(n))
print('O seno é {:.2f}\nseu cosseno é {:.2f}\ntangente {:.2f}'.format(c2, c, c3))