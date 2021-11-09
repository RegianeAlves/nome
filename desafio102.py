def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            if c == 1:
                print('1 = ', end='')
                return f
            print(f'{c} x', end=' ')
    return f


print(fatorial(5, show=True))
# help(fatorial)