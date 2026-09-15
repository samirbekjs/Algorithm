a = int(input())
b = []
k = []
for i  in str(a):
  b.append(int(i))
s = len(b)
for i in b:
    k.append(int(i)**s)
if sum(k) == a:
    print(sum(b))
else:
    print(a)
