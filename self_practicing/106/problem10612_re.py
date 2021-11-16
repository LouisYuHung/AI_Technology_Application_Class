import sys
data = sys.stdin.read()

def test(num:str):
  temp = []
  while len(num) != 0:
    if num[0:2] in inversevalue:
      temp.append(num[0:2])
      num = num[2:]
    else:
      temp.append(num[0])
      num = num[1:]
  return temp

data = data.splitlines()
data = [i[::-1] for i in data]
inversevalue = ['VI', 'XI', 'LX', 'CX', 'DC', 'MC']
for i in range(1, len(data)):
  temp = test(data[i])
  truevalue = {
    'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
    'VI':4, 'XI':9, 'LX':40, 'CX':90, 'DC':400, 'MC':900
  }
  ans = 0
  for i in temp:
    ans += truevalue[i]
  print(ans)