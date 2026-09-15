a = int(input())
n = int(input())
b = []
for i in range(n):
  x,y = map(int,input().split())
  if x == y and x == a:
    b.append("Chiroyli")
  elif x > a and y > a or (x == a and y > a) or (y == a and x >a):
    b.append("Deyarli_chiroyli")
  else:
    b.append("NO")    
print(*b)
