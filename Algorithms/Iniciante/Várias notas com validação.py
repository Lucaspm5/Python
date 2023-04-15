while True:
    temp1 = float(input())
    while temp1 < 0 or temp1 > 10:
        print("nota invalida")
        temp1 = float(input())

    temp2 = float(input())
    while temp2 < 0 or temp2 > 10:
        print("nota invalida")
        temp2 = float(input())

    media = (temp1 + temp2) / 2
    print("media = {:.2f}".format(media))

    opcao = 0
    while opcao != 1 and opcao != 2:
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())
    if opcao == 2:
        break
