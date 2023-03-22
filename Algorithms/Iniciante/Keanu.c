x = int(input())

if x % 2 == 0: 
    aux = (x*x)//2
    sup = aux 
else:
    aux = (x*x)//2
    sup = ((x*x)//2)+1

print(f"{sup} casas brancas e {aux} casas pretas")
