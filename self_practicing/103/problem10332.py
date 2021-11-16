def cutdown(num, Fib):
  i = 0
  while num - Fib[i] < 0:
    i += 1
  return num - Fib[i], Fib[i]
def find(num, Fib):
  tlist = []
  while num > 2:
    ttuple = cutdown(num, Fib)
    num = ttuple[0]
    tlist.append(ttuple[1])
  else:
    if num != 0:
      tlist.append(num)
  return tlist
def answer(tlist, Fib):
  for i in range(len(Fib)):
    if Fib[i] not in tlist:
      Fib[i] = 0
  for i in tlist:
    Fib[Fib.index(i)] = 1
  del Fib[:Fib.index(1)]
  Fib = [str(i) for i in Fib]
  print(dlist[i]+"="+"".join(Fib))

Fib = [1, 2]
for i in range(17):
  Fib.append(Fib[i]+Fib[i+1])
Fib = Fib[::-1]

dlist = ["5","64","20","95","31","30"]

for i in range(0,len(dlist)):
  answer(find(int(dlist[i]), Fib), Fib)