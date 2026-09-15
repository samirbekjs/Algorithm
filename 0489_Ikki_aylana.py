import math
x1,y1,r1 = map(int,input().split())
x2,y2,r2 = map(int,input().split())
d = math.sqrt((x1 - x2)**2 + (y1 - y2 )**2)
R = max(r1,r2)
r = min(r1,r2)
if d + r >= R and d - r <= R:
    print("Yes")
else:
    print("No")
