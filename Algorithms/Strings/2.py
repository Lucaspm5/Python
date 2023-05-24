nome = str(input())

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))

frase = nome.split()

print(len(frase[0]))