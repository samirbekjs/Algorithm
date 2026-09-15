p = int(input())
if p == 2710:
  print("0.00","100.00")
elif p == 21450:
  print("100.00","0.00")
else:
    pal = 2710
    ppl = 21450
    alf = (((ppl - p) * pal) / ((ppl - pal) * p)) * 100
    pf = (((p- pal) * ppl) / ((ppl - pal) * p)) * 100
    print('{:.2f}'.format(pf),'{:.2f}'.format(alf))
