num = []
for _ in range(5):
    n = int(input())
    indice = len(num)
    for i, valor in enumerate(num):
        if n < valor:
            indice = i
            break
    print(f'{n} Adicionado na posicao {indice}')
    num.insert(indice, n)
print(num)