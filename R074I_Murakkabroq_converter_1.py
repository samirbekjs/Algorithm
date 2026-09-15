n = int(input())
a = input()
s = ''
for i in a:
  if i == "w" :
    s += "q"
  elif i == "q":
    s += "p"
  elif i == "r":
    s += "e"
  elif i == "t":
    s += "r"
  elif i == "y":
    s += "t"
  elif i == "u":
    s += "y"
  elif i == "i":
    s += "u"
  elif i == "o":
    s += "i"
  elif i == "p":
    s += "o"
  elif i == "a":
    s += "l"
  elif i == "s":
    s += "a"
  elif i == "d":
    s += "s"
  elif i == "f":
    s += "d"
  elif i == "g":
    s += "f"
  elif i == "h":
    s += "g"
  elif i == "j":
    s += "h"
  elif i == "k":
    s += "j"
  elif i == "l":
    s += "k"
  elif i == "z":
    s += "m"
  elif i == "x":
    s += "z"
  elif i == "c":
    s += "x"
  elif i == "v":
    s += "c"
  elif i == "b":
    s += "v"
  elif i == "n":
    s += "b"
  elif i == "m":
    s += "n"
  elif i == " ":
    s += " "
  elif i == "e":
    s += "w"
print(s)
