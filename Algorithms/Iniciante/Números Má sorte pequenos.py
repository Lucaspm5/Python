n = input()
len_n = len(n)
unlucky = False

for i in range(len_n - 1):
    if n[i] == '1' and n[i + 1] == '3':
        unlucky = True
        break

if unlucky:
    print(n, "es de Mala Suerte")
else:
    print(n, "NO es de Mala Suerte")
