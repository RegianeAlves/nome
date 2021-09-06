frase = 'Curso em Vídeo Python'
print(frase[1:15:2])
print(frase[2::4])
print(frase.upper().count('o'))
print(len(frase))
print(len(frase.strip()))
frase = (frase.replace('Python', 'Android'))
print(frase)
print('Curso' in frase)
dividido = frase.split()
print(dividido[2][3])

