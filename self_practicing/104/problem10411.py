import sys
arti = sys.stdin.read()
dlist = arti.split("\n")

def pricecal(list):
  tlist = [int(i) for i in list[1].split(",")]
  price = 0
  for i in range(int(list[0])-1):
    if tlist[i+1] > tlist[i]:
      price = price + (tlist[i+1]-tlist[i])*20
    else:
      price = price + (tlist[i]-tlist[i+1])*10
  print(price)

dlist[0] = int(dlist[0])
for i in range(1,dlist[0]*2,2):
  plist = dlist[i:i+2]
  pricecal(plist)