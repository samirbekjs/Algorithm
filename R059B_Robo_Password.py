n = int(input())
l = len(str(n))
b = 0
if str(n)[0] != "0":
    for i in str(n):
        b += int(i)
    if l == 9 and b % 2 == 1:
        print("yes")
    else:
        print("no")
else:
    print("no")
