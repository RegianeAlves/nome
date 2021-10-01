times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino',
         'Corinthians', 'Internacional', 'Fluminense', 'Atlético-PR', 'Cuibá',
         'Ceará SC', 'Atlético-GO', 'São Paulo', 'Juventude', 'América-MG',
         'Santos', 'Bahia', 'Grêmio', 'Sport Recife', 'Chapecoense')

print(f'Lista dos times do Brasileirão: {times}')
print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os 4 Últimos são: {times[16:]}')
print(f'Times em ordem alfabetica: {sorted(times)}')
print(f"O Chapecoense está na {times.index('Chapecoense')}ª posição")
