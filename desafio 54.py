from datetime import date
anoatual = date.today().year
contador = 0
contador2 = 0
for c in range(0, 6):
    n = int(input('Digite o ano de nascimento: '))
    idade = anoatual - n
    if idade >= 18:
        contador = contador + 1
    else:
        contador2 = contador2 + 1
print('Maiores de idade: {}'.format(contador))
print('Menores de idade: {}'.format(contador2))




