maior = menor = quantHomens = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        quantHomens += 1
    if idade < 20 and sexo == 'F':
        menor += 1
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {quantHomens} homens cadastrados')
print(f'E temos {menor} mulheres com menos de 20 anos')
