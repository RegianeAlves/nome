contador = soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'A soma entre eles é {soma}\nFoi digitado {contador} números')