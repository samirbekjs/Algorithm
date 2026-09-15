s,a,b,c = map(int,input().split())
s = s % (a+b+c)
if a > s:
    print("Azim")
elif s - a < b:
    print("Aziz")
else:
    print("Akbar")
