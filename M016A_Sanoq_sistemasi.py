k , n = map(int,input().split())
q = []
s = ''
if k < 10 and k < n:
    print(k)
else:
    while True:
      q.append(k % n)
      if k // n >= n:
          k = k // n
      else:
        q.append(k // n)
        break
  
    for i in q :
      if i == 10 :
        s += 'A'
      elif i == 11:
        s+= 'B'
      elif i == 12:
        s += 'C'
      elif i == 13 :
        s += 'D'
      elif i == 14 :
        s += 'E'
      elif i == 15:
        s += 'F'
      else:
        s += str(i)
    print(s[::-1] )
