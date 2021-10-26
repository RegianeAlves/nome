ficha = {}
soma = cont = 0
totgols = []

ficha['nome'] = str(input('Nome do jogador: ')).title()
partidas = int(input(f'     Quantas partidas {ficha["nome"]} jogou: '))

for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c}? '))
    totgols.append(gols)
    ficha['gols'] = totgols
    soma += gols
ficha['total'] = soma

print('-=' * 20)
for key, valor in ficha.items():
    print(f'    O campo {key} tem o valor {valor}.')

print('-=' * 20)
print(f'O jogador {ficha["nome"]} jogou {gols} partidas')
print('-=' * 20)

for v in ficha['gols']:
    print(f'    Na partida {cont}, fez {v} gols')
    cont += 1
print('-=' * 20)

print(f'Foi um total de {soma} gols.')
