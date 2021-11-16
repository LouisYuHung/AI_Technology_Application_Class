import sys
data = sys.stdin.read()

data = data.splitlines()
for i in range(1, len(data)):
  datapart = data[i].split(" ")
  count = 0
  for i in datapart:
    if 's' in i or 'S' in i:
      count += 1
  print(count)