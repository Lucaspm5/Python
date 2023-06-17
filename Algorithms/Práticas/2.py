def verifica_duplicada(num):
    suport = set()
    for item in num:
        if item not in suport:
            suport.add(item)
    return suport
num = []
while True:
    num.append(int(input('Informe um elemento:')))
    print('Deseja continuar (1-sim 2-nao)')
    op = int(input())
    if op == 2: break
pos = verifica_duplicada(num)
num.sort()
print(pos)
