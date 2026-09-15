ys = 0
for i in range(3):
  ys += input().count("*")
print("O" if ys % 2 == 1 else "X")
