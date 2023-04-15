X = int(input())
Y = int(input())

if X > Y:
    for aux in range(Y+1, X):
        if aux % 5 == 2 or aux % 5 == 3:
            print(aux)
elif X < Y:
    for aux in range(X+1, Y):
        if aux % 5 == 2 or aux % 5 == 3:
            print(aux)
