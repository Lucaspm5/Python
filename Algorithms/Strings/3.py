a = int(input())

unidade = a % 10
dezena = a // 10 % 10
centena = (a//10) // 10 % 10
milhar = (((a//10) // 10) // 10) % 10

print(f'Unidade {unidade}')
print(f'Dezena {dezena}')
print(f'Centena {centena}')
print(f'Milhar {milhar}')