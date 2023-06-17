cont = 0
count = 0
positivos = 0
negativos = 0
for i in range(5):
    n = int(input())
    if n % 2 == 0:
        cont += 1
    if n % 2 != 0:
        count += 1
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
print(f'{cont} valor(es) par(es)')
print(f'{count} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')