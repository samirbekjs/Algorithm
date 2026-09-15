a = list(map(int,input().split()))
s = input()
b = []
for i in s:
  b.append(a[ord(i) - 97])
print(max(b) * len(s))
