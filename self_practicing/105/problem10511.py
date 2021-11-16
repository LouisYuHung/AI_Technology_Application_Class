import sys
data = sys.stdin.read()

data = data.splitlines()
for i in range(1, int(data[0]) + 1):
  amount = data[i].count(" ")
  print(amount + 1)