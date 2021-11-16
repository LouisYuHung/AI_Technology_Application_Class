import sys
arti = sys.stdin.read()
dlist = arti.split("\n")

dic = {"00":0,"01":1,"100":2,"101":3,"1100":4,"1101":5,"11100":6,"11101":7,"111100":8,"111101":9}
alpha = "DEFGHIJKLMNOPQRSTUVWXYZABC"

def cut(li):
  i = 0
  while li[:i] not in dic:
    i += 1
  li = [li[:i] , li[i:]]
  return li

for i in range(1, len(dlist)):
  a = cut(dlist[i])
  b = [dic[a[i]] for i in range(2)]
  c = b[0]*10+b[1]
  print(alpha[c-1])