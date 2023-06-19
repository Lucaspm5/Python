def verifica_conjunto(n):
    maior = 0
    copy = []
    for i in range(len(n) - 4):
        produto = int(n[i]) * int(n[i+1]) * int(n[i+2]) * int(n[i+3]) * int(n[i+4])

        if produto > maior:
            maior = produto
            copy = [n[i], n[i+1], n[i+2], n[i+3], n[i+4]]
    return copy 
n = input()
conjunto = verifica_conjunto(n)
print(''.join(map(str, conjunto))) 