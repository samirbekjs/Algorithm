h,m=map(str,input().split(':'))
h1=h[::-1]
if 6<=int(h)<10:
    print('10:01')
elif 16<=int(h)<20:
    print('20:02')
elif h1>m:
  print(f'{h}:{h1}')
else:
  h1=str((int(h)+1)%24).zfill(2)
  print(f'{h1}:{h1[::-1]}')
