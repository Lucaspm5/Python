n = input()

if n[2] == '/' and n[5] == '/':
    print('formatação valida')
dia, mes, ano = n.split('/')

auxiliary = [dia, mes, ano]

aux = True

for elemento in auxiliary:
    if not elemento.isnumeric():
        aux = False
        break

if aux: print('sim')