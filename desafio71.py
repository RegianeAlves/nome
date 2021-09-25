cont50 = cont20 = cont10 = cont1 = 0

while True:
    valor = int(input('Que valor você quer sacar? R$'))
    cont50 = valor // 50
    valor -= cont50 * 50
    cont20 = valor // 20
    valor -= cont20 * 20
    cont10 = valor // 10
    valor -= cont10 * 10
    cont1 = valor // 1
    valor -= cont1 * 1
    if valor == 0:
        break
print(f'Total de {cont50} cédulas de R$50')
print(f'Total de {cont20} cédulas de R$20')
print(f'Total de {cont10} cédulas de R$10')
print(f'Total de {cont1} cédulas de R$1')
