n = int(input())
a = list(map(int,input().split()))
b = [0]*(n + 1)
for i in a:
  b[i] += 1
print(b.index(max(b)))
