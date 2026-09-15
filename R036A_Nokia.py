a = input()
l = 0
b = []
for i in a:
    b.append(i)
for j in b:
    if j == "a" or j == "d" or j == "g" or j == "j" or j == "m" or j == "p" or j == "t" or j == "w" or j == " ":
        l += 1
    elif j == "b" or j == "e" or j == "h" or j == "k" or j == "n" or j == "q" or j == "u" or j == "x":
        l += 2
    elif j == "c" or j == "f" or j == "i" or j == "l" or j == "o" or j == "r" or j == "v" or j == "y":
        l += 3
    elif j == "s" or j == "z":
        l += 4
print(l)
