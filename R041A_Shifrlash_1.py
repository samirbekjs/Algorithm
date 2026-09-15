a = str(input())
x = []
x.append(len(a))
for i in a:
    c = ord(i) - 96
    if c == 1:
        x.append(str(110) + "000" + str(bin(c)[2:]))
    elif c == 2 or c == 3:
        x.append(str(11) +"000" + str(bin(c)[2:]))
    elif c >= 4 and c <= 7:
        x.append(str(11) + "00" + str(bin(c)[2:]))
    elif c >= 8 and c <= 15:
        x.append(str(11) + str(0) + str(bin(c)[2:]))
    else:
        x.append(str(11) + str(bin(c)[2:]))
for i in x:
    print(i)
