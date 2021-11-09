from datetime import date


def voto(n):
    if n < 16:
        return 'NEGADO!'
    elif 16 <= n < 18:
        return 'OPCIONAL!'
    elif 18 <= n < 65:
        return 'OBRIGATORIO!'
    else:
        return 'OPCIONAL!'


ano = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
idade = anoatual - ano
print(f'Com {idade} anos: VOTO {voto(idade)}')
