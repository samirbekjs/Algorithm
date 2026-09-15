n = int(input())
for i in range(n):
    b= int(input())
    k = 5
    cnt = 1
    t = 0
    while b > k:
        cnt += 1
        k += 5 ** cnt
    print(cnt)
