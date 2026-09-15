n = int(input())
a = list(map(int,input().split()))
b = [0] * 101
for i in a:
  b[i] += 1
maximum = max(b)
print(n - maximum)
