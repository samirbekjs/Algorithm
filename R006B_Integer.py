def top(n):
    bn = bin(n)[2:]
    qs = "0" * (32 - len(bn))
    qiymat = qs + bn
    return qiymat
def lsq(arr):
    st = ''
    for i in arr:
        i = int(i)
        st += ["1","0"][i]
    return st
n = int(input())
if n >= 0:
    print(top(n))
else:
    n = -n
    print(bin(int(lsq(top(n)),2) + 1)[2:])
