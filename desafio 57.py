s = str(input('Digite seu sexo: [M/F]: ')).upper()
while s != 'M' and s != 'F':
    print('Aceitamos apenas M ou F, Por favor digite novamente!')
    s = str(input('Digite seu sexo: [M/F]: ')).upper()
print('Obrigada!')