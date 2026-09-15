n = input()
if n[0] != "-":
    if n[0] == "0" and n[1] == "x":
        unolt = n[2:]
        print(int(unolt,16))
    elif n[0] == "0" and n[1] != "x":
        sakkiz = n[1:]
        print(int(sakkiz,8))
    else:
        print(n)
else:
    n = n[1:]
    if n[0] == "0" and n[1] == "x":
        unolt = n[2:]
        print(int(unolt,16) * (-1))
    elif n[0] == "0" and n[1] != "x":
        sakkiz = n[1:]
        print(int(sakkiz,8) * (-1))
    else:
        print(int(n)*(-1))
