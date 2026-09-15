satr = list(input())
s=""
for i in range(len(satr)-1):
    if ((satr[i]=='s' or satr[i]=='c') and satr[i+1]=='h') or (satr[i]=='n' and satr[i+1]=='g'):
        satr[i],satr[i+1]=satr[i+1],satr[i]
for i in range(len(satr)-1,-1,-1):
    print(satr[i],end='')
