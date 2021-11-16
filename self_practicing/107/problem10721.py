import sys
data = sys.stdin.read()

def testhappy(num:str):
  num = int(num)
  temp = [num]
  while temp[-1] != 1 and temp[-1] not in temp[:-1]:
    a = str(temp[-1])
    num = 0
    for i in range(len(a)):
      num += int(a[i]) ** 2
    temp.append(num)
  if temp[-1] == 1:
    print('T')
  else:
    print('F')

data = data.splitlines()
for i in range(1, len(data)):
  testhappy(data[i])