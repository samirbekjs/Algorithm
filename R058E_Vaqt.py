a,b = map(int,input().split(":"))
n = int(input())
a1 = b + n
x = "0"
if a1 >= 60:
  a1 -= a1 // 60 * 60
  a += (b + n) // 60
if a >= 24:
  a -= a // 24 * 24
if a < 10 and a1 < 10:
    a = str(a)
    a1 = str(a1)
    print(f"{x+a}:{x+a1}")
elif a >= 10 and a1 < 10:
    a1 = str(a1)
    print(f"{a}:{x+a1}")
elif a < 10 and a1 >= 10:
    a = str(a)
    print(f"{x+a}:{a1}")
else:
    print(f"{a}:{a1}")
