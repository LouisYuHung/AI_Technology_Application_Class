import sys
data = sys.stdin.read()

def findroute(num, tlist):
  temp = list([num])
  while num != 999:
    temp.append(tlist[num])
    num = tlist[num]
    # print(temp)
  return len(temp) - 2

def findans(data):
  def addtocol(list, j):
    collist1 = [i[j] for i in list]
    collist.append(collist1)
    
  rowlist = []
  collist = []
  tree = int(datapart[0].split(",")[1])
  num = int(datapart[0].split(",")[2])
  for i in datapart[1:]:
    templist = i.split()
    rowlist.append([int(i) for i in templist])
  for j in range(1, tree + 1):    
    addtocol(rowlist, j)
  ans = []
  for i in range(tree):
    ans.append(findroute(num, collist[i]))
  ans = [str(i) for i in ans]
  print(",".join(ans))

data = data.splitlines()
# print(data)
while len(data) > 1:
  pdatai = data[1].split(",")
  datarow = int(pdatai[0])
  datapart = data[1:datarow+2]
  # print(datapart)
  findans(datapart)
  del data[1:datarow+2]
  # print(data)