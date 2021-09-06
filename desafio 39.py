from datetime import date

ano = int(input('Digite o ano de nascimento: '))
a = date.today().year
c = a - ano
s = 18 - c
s2 = c - 18
if c < 18:
    print('Você tem {} anos, ainda falta {} anos para se alistar'.format(c, s))
elif c == 18:
    print('Você tem {} anos, está na hora de se alistar'.format(c))
else:
    print('Você tem {} anos, já passou {} anos do tempo de se alistar'.format(c, s2))
