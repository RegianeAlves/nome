ficha = {}

ficha['Nome'] = str(input('Nome: ')).title()
ficha['Média'] = float(input(f'Média de {ficha["Nome"]}: '))

# print(f'Nome é igual a {ficha["nome"]}')
# print(f'Média é igual a {ficha["media"]}')

if ficha['Média'] >= 7:
    ficha['Situação'] = 'Aprovado'
elif 5 <= ficha['Média'] < 7:
    ficha['Situação'] = 'Recuperação'
else:
    ficha['Situação'] = 'Reprovado'

for key, valor in ficha.items():
    print(f'{key} é igual a {valor}')