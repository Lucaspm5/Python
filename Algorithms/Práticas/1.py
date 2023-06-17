num = []
for _ in range(5):
    n = int(input())
    num.append(n)
maior = max(num)
menor = min(num)
for aux, ent in enumerate(num):
    if ent == maior:
        print(f'Indice:{aux} - maior:{maior}')
    if ent == menor:
        print(f'Indice:{aux} - menor:{menor}')