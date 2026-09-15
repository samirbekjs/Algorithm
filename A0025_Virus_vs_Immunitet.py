n = int(input())
a = list(map(int,input().split()))
a.sort()
t = int(input())
b = []
for i in range(t):
    b.append(int(input()))
for i in b:
    cnt = 0
    x = 0
    for j in a:
        if i >= j:
           cnt += 1
           x += 1
        else:
            x += 1
    if x == n:
        print(cnt)
        x = 0
        cnt = 0
