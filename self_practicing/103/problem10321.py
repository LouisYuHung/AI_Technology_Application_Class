import sys
arti = sys.stdin.read()
datalist = arti.split("\n")

def printout(str1,str2):
  s1 = set(str1)
  s2 = set(str2)
  common = []
  for i in s2:
    if i in s1:
      common.append(i)
  common.sort()
  if common != []:
    print("".join(common))
  else:
    print("N")

for i in range(int(datalist[0])):
  printout(datalist[2*i+1],datalist[2*i+2])