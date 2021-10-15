valores = []
cont = 0

while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
if valores.count(5) != 0:
    print('O valor 5 faz parte dessa lista!')
else:
    print('O valor 5 não foi encontrado na lista')

# valor = valores.count(5)
# if valor != 0:
#     print('O valor 5 faz parte dessa lista!')
# else:
#     print('O valor 5 não foi encontrado na lista')


# if 5 in valores:
#     print('O valor 5 faz parte dessa lista!')
# else:
#     print('O valor 5 não foi encontrado na lista')

valores.sort(reverse=True)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
