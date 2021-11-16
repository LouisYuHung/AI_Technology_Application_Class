import sys
data = sys.stdin.read()
# data = '''5
# 1234567891234563
# 4013735633800642
# 5181271099000017
# 5241150318192904
# 5241150313182900''' 

data = data.splitlines()
for j in range(1, len(data)):
  temp = []
  for i in range(16):
    if i % 2 == 0:
      temp.append(int(data[j][i]) * 2)
    else:
      temp.append(int(data[j][i]))
    if temp[i] >= 10:
      temp[i] = int(temp[i]) - 9
  test = sum(temp)
  if test % 10 == 0:
    print('T')
  else:
    print('F')