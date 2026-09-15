n = int(input())
if n == 1918:
    print('26.09.'+ str(n))
elif n > 1918:
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        print(f"12.09.{n}")
    else:
        print(f"13.09.{n}")
else:
    if n % 4 == 0:
        print(f"12.09.{n}")
    else:
        print(f"13.09.{n}")
