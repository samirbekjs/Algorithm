import math as s
t = int(input())
x = 1000000007
for i in range(t):
  t -=1
  n,m = map(int,input().split())
  c = s.factorial(n+m-1)//(s.factorial(m)*s.factorial(n-1))%x
  print(c)
