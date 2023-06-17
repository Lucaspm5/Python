n = []
for i in range(5):
    n.append(int(input()))
maior = max(n)
for i, value in enumerate(n):
    if value == maior:
        print(maior)
        print(i+1)