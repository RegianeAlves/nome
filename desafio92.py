from datetime import date
dados = {}

dados['Nome'] = str(input('Nome: ')).title()
ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
dados['Idade'] = idade
dados['Carteira'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['Carteira'] != 0:
    dados['Ano'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    contrat = (dados['Ano'] - ano) + 35
    dados['Aposentadoria'] = contrat

print(dados)

for key, valor in dados.items():
    print(f'{key} tem o valor {valor}')
