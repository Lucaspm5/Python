n = []
diamantes_possiveis = 0
count = 0
cases = int(input())
for _ in range(cases):
    diamantes_possiveis = 0
    diamante = input()
    for i in range(len(diamante)):
        if diamante[i] == '<':
            n.append(diamante[i])
            count += 1
        elif diamante[i] == '>' and count >= 1:
            n.pop()
            diamantes_possiveis += 1
    print(diamantes_possiveis)