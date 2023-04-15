x = int(input())
y = []
for aux in range(x):
    y.append(int(input()))
for aux in range(x):
    print("resposta {}: {}".format(aux+1, y[aux]))
