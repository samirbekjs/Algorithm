n = input()
if n.isnumeric():
    print("Int")
else:
    if "." in n and n[-1] != "." and n[0] != ".":
        d = 0
        for i in n:
            if i == ".":
                d += 1
                if d == 2:
                    print("Str deb")
                    break
            else:
                if not i.isnumeric():
                    d += 1
                    print("Str deb")
                    break
        if d == 1:
            print("Float")
    else:
        print("Str deb")
