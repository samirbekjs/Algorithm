a,b=map(int,input().split())
cnt = 0
while cnt != b:
    if a % 10 != 0:
        a = a - 1
        cnt += 1
    else:
        a = a // 10
        cnt += 1
print(a)
