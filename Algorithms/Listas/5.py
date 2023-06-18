def cria_sequencia(n):
    auxiliary = [0]
    for i in range(1, n+1):
            for j in range(i):
                auxiliary.append(i)
    return auxiliary
count = 0 
size = 0
while True:
    try:
        count += 1
        n = int(input())
        sequencia = cria_sequencia(n)
        size = len(sequencia)
        if size <= 1:
            print(f'Case {count}: {size} numero')
            print(' '.join(map(str, sequencia)))
            print()
        else:
            print(f'Case {count}: {size} numeros')
            print(' '.join(map(str, sequencia)))
            print()
    except EOFError:
        break