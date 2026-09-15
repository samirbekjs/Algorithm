n = int(input())
l = len(str(n))
o = "9"
mx = int(o * l)
s = 0
for i in range(l):
  s += (9 * 10 ** i) * (i + 1)
print(s - (mx - n) * l)
