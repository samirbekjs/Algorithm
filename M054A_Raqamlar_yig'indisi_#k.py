n,k = map(int,input().split())
a = []
while True:
  a.append(n%k)
  n = n // k
  if n < k:
      a.append(n)
      break
print(sum(a))
