n=int(input())
x = 0
for i in range(n):
  b = input()
  if b == "X++" or b == "++X":
    x += 1
  else:
    x -= 1
print(x)
