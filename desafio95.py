lista = []
ficha = {}
soma = cont = 0
totgols = []

while True:
    ficha.clear()
    ficha['nome'] = str(input('Nome do jogador: ')).title()
    partidas = int(input(f'Quantas partidas {ficha["nome"]} jogou: '))
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {c}? '))
        totgols.append(gols)
        soma += gols
    ficha['gols'] = totgols[:]
    totgols.clear()
    ficha['total'] = soma
    soma = 0
    lista.append(ficha.copy())
    continuar = str(input('Quer continuar: [S/N] ')).upper()[0]
    if continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N] ')).upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'{"Cod nome":<15}{"gols":<10}{"total":>8}')
print('-' * 60)
for indice, dicionario in enumerate(lista):
    print(indice, end=' ')
    for key, valor in dicionario.items():
        print(valor, end='      ')
    print()

while True:
    partida = 0
    print('-' * 35)
    opc = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    for indice, dicionario in enumerate(lista):
        if opc == indice:
            print(f'-- LEVANTAMENTO DO JOGADOR {dicionario["nome"]}')
            for valor in dicionario['gols']:
                print(f'    -> No jogo {partida} fez {valor}')
                partida += 1
    if opc == 999:
        print('FINALIZANDO...')
        break
    elif opc >= len(lista) or opc < 0:
        print(f'ERRO! Não existe jogador com código {opc}. Tente novamente')


