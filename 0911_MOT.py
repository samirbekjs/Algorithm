x1,y1 = map(int,input().split())
x2,y2 = map(int, input().split())
if abs(x1 - x2) == abs(y1 - y2) or (x1!= x2 and y1 == y2) or (y1 != y2 and x1 == x2):
    print("game over")
else:
    print("game")
