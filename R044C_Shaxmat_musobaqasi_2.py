n = int(input())
a,b = map(float,input().split())
if a + b == n:
  if (a % 1 == 0 and b % 1 == 0) or (a % 1 == 0.5 and b % 1 == 0.5):
  	print("YES")
  else:
    print("NO")
else:
  print("NO")
