
# Se o ano não for terminado em 00, e for divisivel por 4 ele eh bissexto
# Se o ano for terminado em 00, e for divisivel por 400 ele eh bissexto
# se ele não atender as essas condições, ele não bissexto
n = int(input('Digite o ano: '))
if n % 100 == 0:
    if n % 400 == 0:
        print('Ele é um ano bissexto')
    else:
        print('Ele não é ano bissexto')
else:
    if n % 4 == 0:
        print('Ele é um ano bissexto')
    else:
        print('Ele não é ano bissexto')
