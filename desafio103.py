def ficha(n='', g=''):
    if n == '' and g == '':
        print('O jogador <desconhecido> fez 0 gol(s) no campeonato.')
    elif g == '':
        print(f'O jogador {n} fez 0 gol(s) no campeonato.')
    elif n == '':
        print(f'O jogador <desconhecido> fez {g} gol(s) no campeonato.')
    else:
        print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
ficha(nome, gols)
