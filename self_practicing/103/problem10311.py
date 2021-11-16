import sys
arti = sys.stdin.read()
def primetest(num):
  i = 2
  while num % i != 0:
    i += 1
  if i == num:
    judge = True
  else:
    judge = False
  return judge
def duotest(num):
  if primetest(num) and primetest(num+2) == True:
    print("Y")
  else:
    print("N")
datalist = arti.split("\n")[1:]
for i in datalist:
  num = i[:i.index(",")]
  duotest(int(num))

