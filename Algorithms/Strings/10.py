cases = int(input())

for _ in range(cases):
    soma = 0
    index = []
    n = input().split()
    x, y = map(int, input().split())
    soma = x + y
    if soma % 2 == 0:
        index = n.index('PAR')
        print(n[index-1])
    if soma % 2 != 0:
        index = n.index('IMPAR')
        print(n[index-1])
        