cases = int(input())
n = []
auxiliary = list(map(int, input().split()))
for i in range(cases):
    n.insert(i, auxiliary[i])
menor = min(n)
index = n.index(menor)
print(f'Menor valor: {menor}')
print(f'Posicao: {index}')
