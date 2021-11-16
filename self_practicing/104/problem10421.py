import sys
arti = sys.stdin.read()
dlist = arti.split("\n")
import math
import random


def find(stri):
  ntlist = [i for i in stri]
  total = math.factorial(len(stri))
  tset = set({})
  while len(tset) != total:
    random.shuffle(ntlist)
    tstr = ""
    for i in range(len(ntlist)):
      tstr = tstr + ntlist[i]
    tset.add(tstr)
  return [int(i) for i in sorted(list(tset))]

for i in range(1, int(dlist[0])+1):
  tlist = dlist[i].split(",")
  allele = find(tlist[0])
  num1 = allele[int(tlist[1])-1]
  num2 = allele[int(tlist[2])-1]
  print(num1+num2)