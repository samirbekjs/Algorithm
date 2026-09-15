s,p = map(int,input().split())
d = (s ** 2 - 4 * p)
if d >= 0:
    d = d ** (0.5)
    x1 = (s + d) // 2
    x2 = (s - d) // 2
    if (s + d) % 2 == 0 and (s - d) % 2 == 0: 
        print(round(x1),round(x2))
    else:
        print(-1)
else:
    print(-1)
