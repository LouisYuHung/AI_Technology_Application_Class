import sys
data = sys.stdin.read()

def cut(num):
  i = 0
  while num - powertwo[i] < 0:
    i += 1
  return num - powertwo[i], i

powertwo = []
for i in range(17):
  powertwo.append(2**i)
powertwo = powertwo[::-1]

data = data.splitlines()
data = [int(i) for i in data]
for num in data[1:]:
  ans = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
  while num != 0:
    ttuple = cut(num)
    ans [ttuple[1]] = "1"
    num = ttuple[0]
  print(ans.count("1"))