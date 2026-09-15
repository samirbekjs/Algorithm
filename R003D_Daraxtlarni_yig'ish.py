n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
for i in a:
  print(str(bin(i)[2:]).count("1"))
