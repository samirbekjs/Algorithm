text = input()
cnt = 0
o = text.count("o")
z = text.count("z")
for i in range(len(text) - 1):
  if text[i] != text[i + 1]:
    cnt += 1
if o / 2 == z and text[0] == "z" and cnt == 1:
  print("Yes")
else:
  print("No")
