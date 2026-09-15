n = int(input())
for i in range(0,n):
  ax,ay,bx,by = map(int,input().split())
  print(2 * bx - ax,2 * by - ay)
