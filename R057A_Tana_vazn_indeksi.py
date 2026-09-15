v , b = map(int,input().split())
s = (10000 * v)/ b**2
if s < 16:
  print("Yuqori vazn yetishmasligi")
elif 16 <= s and s < 18.5 :
  print("Vazn yetishmasligi")
elif 18.5 <= s and s <= 25 :
  print("Ideal vazn")
elif 25 < s and s <= 30:
  print("Ortiqcha vazn")
elif 30 < s and s <= 35:
  print("Semizlikning I darajasi")
elif 35 < s and s <= 40:
  print("Semizlikning II darajasi")
elif 40 < s :
  print("Semizlikning III darajasi")
