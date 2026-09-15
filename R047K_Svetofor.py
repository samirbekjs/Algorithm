n=int(input())
k=n%50
k += 1
if k>0 and k<26:
    print('O__')
elif k>25 and k<30:
    print('OO_')
elif k>29 and k<36:
    print('_O_')
else:
    print('__O')
