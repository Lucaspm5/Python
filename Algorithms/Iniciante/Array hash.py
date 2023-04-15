size = int(input())

for _ in range(size):
    n = 0
    l = int(input())
    support = []
    for i in range(l):
        support.append(input())

    for i in range(l):
        for j in range(len(support[i])):
            n += ((ord(support[i][j]) - 65) + i + j)

    print(n)
