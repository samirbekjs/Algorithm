import math
n = int(input())
s = []
k = 0
cnt = 0
for i in range(2,n +1):
  for j in range(2,int(math.sqrt(i))+1):
    if i % j == 0:
      break
  else:
    s.append(i)
for i in s:
  for j in s:
    if i + j == n :
      cnt += 1
print(cnt)
