n = int(input())
dic = {}
for i in range(n):
    a,b = input().split()
    b = int(b)
    if a in dic:
        dic[a] += b
    else:
        dic[a] = b
m = int(input())
for i in range(m):
    x = input()
    print(x,dic[x])
