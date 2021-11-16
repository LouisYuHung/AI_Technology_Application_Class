import sys
arti = sys.stdin.read()
dlist = [int(i) for i in arti.splitlines()]

Fib = [1, 2]
i = 0
while i < 17:
  Fib.append(Fib[i] + Fib[i + 1])
  i += 1

def cut(num):
  i = 0
  while Fib[i] <= num:
    i += 1
  num = num - Fib[i-1]
  return num, Fib[i-1], i-1


for i in range(1, len(dlist)):
  num = dlist[i]

  nlist = []
  Flist = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

  while num != 0:
    tlist = cut(num)
    nlist.append(tlist[1])
    num = tlist[0]
    Flist[18 - tlist[2]] = "1"

  Flist = Flist[Flist.index("1"):]
  print(f'{dlist[i]}={"".join(Flist)}')