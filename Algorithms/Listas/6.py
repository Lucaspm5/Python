count = 0
while True:
    try:
        x = input()
        y = input()
        count += 1
        if y.count(x) >= 1:
            print(f'Caso #{count}:')
            print('Qtd.Subsequencias: {}'.format(y.count(x)))
            print('Pos {}'.format(y.rfind(x)+1))
            print()
        else:
            print('Caso #{count}:')
            print('Nao existe subsequencia')
    except EOFError:
        break