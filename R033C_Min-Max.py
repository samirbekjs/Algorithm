n = int(input())
r = int(input())
k = int(input())
s = []
for i in range(n , r+ 1):
    l = 0
    for j in str(i):
        l += int(j)
    if l == k:
        s.append(i)
print(min(s))
print(max(s))
