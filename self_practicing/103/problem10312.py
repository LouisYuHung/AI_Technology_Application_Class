import sys
arti = sys.stdin.read()
datalist = arti.split("\n")[1:]
import math
def solve(total, num1, num2, price):
  for x in range(math.ceil(price/num1)+1):
    for y in range(math.ceil(price/num2)+1):
      if x + y == total and num1 * x + num2 * y == price:
        print(str(x)+","+str(y))
for i in datalist:
  j = i.split(",")
  for k in range(len(j)):
    j[k] = int(j[k])
  solve(j[0],j[1],j[2],j[3])