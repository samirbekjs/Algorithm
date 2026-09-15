text = input()
if text[0] == "0":
  cnt = 0
  for i in range(len(text) - 1):
    if text[i] != text[i + 1]:
      cnt += 1
  if cnt <= 2:
    print("YES")
  else:
    print("NO")
else: 
  cnt = 0
  for i in range(len(text) - 1):
    if text[i] != text[i + 1]:
      cnt += 1
  if cnt < 2:
    print("YES")
  else:
    print("NO")
