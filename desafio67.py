while True:
    n = int(input('Quer ver a taboada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        mult = n * c
        print(f'{n} x {c} = {mult}')
print('Taboada encerrada!')



