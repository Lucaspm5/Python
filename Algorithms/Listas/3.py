cont = 0
soma = 0
while True:
    n = input()
    if n[0] == '*':
        soma += 4
    if n[1] == '*':
        soma += 2
    if n[2] == '*':
        soma += 1
    if n[0] == 'c':
        print(soma)
        soma = 0
        cont += 1
    if cont == 3: break

