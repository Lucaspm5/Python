def binario(n):
    if n != 0:
        return str(n%2) + binario(n//2)
    return 
n = int(input())
x = binario(n)
print(x[::-1])