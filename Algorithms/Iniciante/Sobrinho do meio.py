h, z, l = map(int, input().split())

if h > z:
    if h < l:
        print("huguinho")
    elif l > z:
        print("luisinho")
    else:
        print("zezinho")
elif z < l:
    print("zezinho")
elif l > h:
    print("luisinho")
else:
    print("huguinho")
