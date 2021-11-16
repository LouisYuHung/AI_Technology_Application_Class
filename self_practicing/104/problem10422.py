import sys
arti = sys.stdin.read()
dlist = arti.split("\n")

def findfac(num):
  facl = set({})
  for i in range(1, num+1):
    if num % i == 0:
      facl.add(i)
  return facl

def findmaxcofac(stri):  
  set1 = [int(i) for i in stri.split(",")]
  setfac = [findfac(i)for i in set1]
  i = 0
  while i < len(setfac)-1:
    tset = setfac[i]&setfac[i+1]
    i += 1
  print(max(tset))

for i in dlist[1:]:
  findmaxcofac(i)