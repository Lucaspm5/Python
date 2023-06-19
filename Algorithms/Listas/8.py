lista = [0] * 20
par = []
impar = []

for i in range(20):
    lista[i] = i

for value in lista:
    if value % 2 == 0:
        par.append(value)
    else:
        impar.append(value)
print(par)
print(impar)