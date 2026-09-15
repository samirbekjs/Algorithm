import math
x1,y1 = map(int ,input().split())
x2,y2 = map(int ,input().split())
x3,y3 = map(int ,input().split())
a = math.sqrt((x1 - x2)**2 + (y1 -y2)**2)
b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
if a + b <= c or a + c <= b or b + c <= a:
  print("uchburchak emas")
else:
  print("uchburchak")
