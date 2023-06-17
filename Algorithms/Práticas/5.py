num = []
for _ in range(6):
    num.append(int(input()))
cont = 0
for i in range(6):
    if num[i] >= 0:
        cont += 1
print(f'{cont} valores positivos')