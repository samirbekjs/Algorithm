n = int(input())
if n > 0:
    for i in range(0,n + 1): 
        print(i)
else:
    n = n * (-1)
    for i in range(0,n + 1):
        print(i * (-1))
