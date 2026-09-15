n = int(input())
l = len(str(n))
s = 0
cnt = 0
x = "9"
ts = int(x * l)
for i in range(l):
    s += (9 * 10 ** cnt) * (cnt + 1) 
    cnt += 1
print(s - (ts - n) * l)
