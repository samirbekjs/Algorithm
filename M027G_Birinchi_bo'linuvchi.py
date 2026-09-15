n, k = map(int,input().split())
if n > k and n % k ==0:
  print(n)
elif n > k and n % k != 0:
  a = n // k 
  b = n - a*k
  c= k -b
  print(c +n)
elif n < k and k % n == 0 :
  print(k)
elif n < k and k % n != 0:
  a1 = k - n 
  print(a1 + n)
elif n == k:
  print(n)
