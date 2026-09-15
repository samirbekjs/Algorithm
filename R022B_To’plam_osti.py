n = int(input())
a = list(map(int,input().split()))
b = [0]*101
for i in a:
    b[i] += 1
x = []
for i in range(len(b)):
    for j in range(len(b)):
        if abs(i-j) == 1 :
            x.append(b[i]+b[j])
print(max(x))
