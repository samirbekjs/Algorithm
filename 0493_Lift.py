t=int(input())
for i in range(t):
  a,b,n=map(int,input().split())
  if a>=n and b>=n:
    if a>b:
      print("Azimjon")
    elif a==b:
      print("Draw!")
    else:
      print("Maqsud")
  elif a>=n:
    print("Maqsud")
  elif b>=n:
    print("Azimjon")
  else:
    print("Draw!")
