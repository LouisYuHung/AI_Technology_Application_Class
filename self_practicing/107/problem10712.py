import sys
data = sys.stdin.read()

data = data.splitlines()
for i in range(int(data[0])):
  datapart = data[3 * i + 1:3 * i + 4]
  temp = []
  for i in range(len(datapart)):
    for j in range(3):
      temp.append(datapart[i][j])
  if temp[0] == temp[1] == temp[2] == '1':
    print('1')
  elif temp[0] == temp[1] == temp[2] == '2':
    print('2')
  elif temp[3] == temp[4] == temp[5] == '1':
    print('1')
  elif temp[3] == temp[4] == temp[5] == '2':
    print('2')
  elif temp[6] == temp[7] == temp[8] == '1':
    print('1')
  elif temp[6] == temp[7] == temp[8] == '2':
    print('2')
  elif temp[0] == temp[3] == temp[6] == '1':
    print('1')
  elif temp[0] == temp[3] == temp[6] == '2':
    print('2')
  elif temp[1] == temp[4] == temp[7] == '1':
    print('1')
  elif temp[1] == temp[4] == temp[7] == '2':
    print('2')
  elif temp[2] == temp[5] == temp[8] == '1':
    print('1')
  elif temp[2] == temp[5] == temp[8] == '2':
    print('2')
  elif temp[0] == temp[4] == temp[8] == '1':
    print('1')
  elif temp[0] == temp[4] == temp[8] == '2':
    print('2')
  elif temp[2] == temp[4] == temp[6] == '1':
    print('1')
  elif temp[2] == temp[4] == temp[6] == '2':
    print('2')
  else:
    print('3')