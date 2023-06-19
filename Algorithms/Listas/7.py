n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(n[1:10])
print(n[8:14])
print(n[0::2])
print(n[1::2])
print(n[::-1])
aux = n[10:16]
sup = n[3:11]
sum_aux = sum(aux)
sum_sup = sum(sup)

print('{:.4}'.format(sum_aux/sum_sup))
