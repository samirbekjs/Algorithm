n = int(input())
a = list(map(int,input().split()))
x = ""
for i in a:
  s = ((1 + 8 * i) ** (1 / 2) - 1) / 2
  y = s % 1
  if y == 0:
    x += "1"
  else:
    x += "0"
print(x)
