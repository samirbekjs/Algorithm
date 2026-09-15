import math
x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())
d = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
a = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
b = math.sqrt((x4 - x2)**2 + (y4 - y2)**2)
c = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
f = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
p1 = (f + c + d) / 2
s1 = math.sqrt(abs(p1 * (p1 - f) * (p1 - c) * (p1 - d)))
p2 = ( a + b + d) / 2
s2 = math.sqrt(abs(p2 * (p2 - a) * (p2 - b) * (p2 - d)))
print('{:.1f}'.format(s1 + s2))
