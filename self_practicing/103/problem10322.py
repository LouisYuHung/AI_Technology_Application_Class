import sys
arti = sys.stdin.read()
datalist = arti.split("\n")

def compare(s1,s2):
  comf = []
  for i in s2:
    if i in s1:
      comf.append(i)
  print(len(comf))
def turnin(li):
  li = li.split()
  for i in range(1,len(li)):
    li[i] = int(li[i])
  li = set(li[1:])
  return li

for i in range(1, len(datalist), 2):
  s1 = turnin(datalist[i])
  s2 = turnin(datalist[i+1])
  compare(s1, s2)