a = list(map(int,input().split()))
s = 1
if len(a) == 1:
    x = int(input())
    print(a[0] * x)
else:
    print(sum(a))
