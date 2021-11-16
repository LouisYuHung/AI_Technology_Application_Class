import sys
data = sys.stdin.read()
# data = '''4
# 1234,15,9
# 1234,3,4
# 1234,1,24
# 1234,1,1'''

import random
import math
def find(stri):
  ntlist = [i for i in stri]
  total = math.factorial(len(stri))
  tset = set({})
  while len(tset) != total:
    random.shuffle(ntlist)
    tstr = ""
    for i in range(len(ntlist)):
      tstr = tstr + ntlist[i]
    tset.add(tstr)
  return [int(i) for i in sorted(list(tset))]

data = data.splitlines()
for j in range(1, len(data)):
  data[j] = data[j].split(',')
  temp = find(data[j][0])
  num1 = str(temp[int(data[j][1]) - 1])
  num2 = str(temp[int(data[j][2]) - 1])
  aandb = [0, 0]
  for i in range(len(num1)):
    if num1[i] == num2[i]:
      aandb[0] += 1
    else:
      aandb[1] += 1
  print(str(aandb[0]) + 'A' + str(aandb[1]) + 'B')