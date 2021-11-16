import sys
data = sys.stdin.read()

def binary(num):
  ans = []
  if num == 0:
    ans.append('0')
  else:
    while num != 0:
      ans.append(str(num % 2))
      num = num // 2
  while len(ans) != 8:
    ans.append('0')
  ans = ans[::-1]
  return ans

def bi_return(list_8):
  ans = 0
  for i in range(8):
    ans += int(list_8[i]) * (2 ** (7-i))
  return str(ans)

def findanswer(datapart:str):
  datapart = datapart.split('/')
  datapart[0] = [int(i) for i in datapart[0].split('.')]
  datapart[1] = [int(i) for i in datapart[1].split('.')]
  list1 = binary(datapart[0][0]) + binary(datapart[0][1]) + binary(datapart[0][2]) + binary(datapart[0][3])
  list2 = binary(datapart[1][0]) + binary(datapart[1][1]) + binary(datapart[1][2]) + binary(datapart[1][3])
  temp = []
  for i in range(32):
    if list1[i] == '1' and list2[i] == '1':
      temp.append(list1[i])
    else:
      temp.append('0')
  intersection = []
  intersection.append(bi_return(temp[:8]))
  intersection.append(bi_return(temp[8:16]))
  intersection.append(bi_return(temp[16:24]))
  intersection.append(bi_return(temp[24:]))
  print(".".join(intersection))

data = data.splitlines()
for i in range(1, len(data)):
  findanswer(data[i])