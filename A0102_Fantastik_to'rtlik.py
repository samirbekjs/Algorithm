a = list(map(int,input().split()))
a.sort()
if a[-1] - a[-2] == a[-2] - a[0]:
  print(a[-1] + a[-2] - a[0])
elif (a[-2] - a[0]) // (a[-1] - a[-2]) == 2 and (a[-2] - a[0]) % (a[-1] - a[-2]) == 0:
  print(a[0] + a[-1] - a[-2])
elif (a[-1] - a[-2]) // (a[-2] - a[0]) == 2 and (a[-1] - a[-2]) % (a[-2] - a[0]) == 0:
  print(a[1] + a[-2] - a[0])
else:
  print(a[2] + a[1] - a[0])
