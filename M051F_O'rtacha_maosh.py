n = int(input())
a = list(map(int,input().split()))
k =(sum(a) - (min(a) + max(a)))/(n-2)
if k % 1 != 0:
  print( "{:.05f}".format(k))
else: 
  print(round(k))
