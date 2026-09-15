import math
x,y = map(float,input().split())
a = (((x + (2 / x ** 2) + (3 / x **3))) ** (-1)) + ((math.e) ** (x ** 2 + 3 * x))
b = math.atan(x + y) + (abs(5 + x)) ** 2
birinchi_kasr = a / b
ikkinchi_qism = (math.cos(y ** 2 + (x ** 2 / 2))) ** 2
f = birinchi_kasr - ikkinchi_qism
print('{:.2f}'.format(f))
