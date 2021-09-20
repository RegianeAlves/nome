n = int(input('Digite um número: '))

fib = 0
aux = 0
contador = 0
while contador != n:
    print(fib)
    fib = fib + aux
    aux = fib - aux
    contador += 1
    if fib == 0:
       fib += 1