import sys
data = sys.stdin.read()
# data = '''3
# A,B,6 A,E,9 B,C,3 B,D,5 C,D,7 B,F,8 D,E,10 D,F,11 A,F,12 E,F,15
# A,B,3 A,C,2 B,C,1 B,D,2 C,D,1 B,E,2 C,F,1 D,E,1 D,F,1 D,G,2 E,G,1 F,G,1
# A,B,3 B,C,6 C,D,12 D,E,7 A,E,1 A,F,2 F,B,3 F,C,4 F,D,1'''

def findans(datapart:str):
  datapart = datapart.split(' ')
  datapart = [i.split(',') for i in datapart]
  for i in datapart:
    i[0], i[1], i[2] = i[2], i[0], i[1]
    i[0] = int(i[0])
  datapart.sort()
  pointlist = [set(datapart[0][1:]), set(datapart[1][1:])]
  if pointlist[0] & pointlist[1] != set({}):
    pointlist.append(pointlist[0] ^ pointlist[1])
  ans = [datapart[0][0], datapart[1][0]]
  for i in range(2, len(datapart)):
    if set(datapart[i][1:]) in pointlist:
      pass
    else:
      for j in range(len(pointlist)):
        if len(set(datapart[i][1:]) & pointlist[j]) == 0:
          if set(datapart[i][1:]) not in pointlist:
            pointlist.append(set(datapart[i][1:]))
        else:
          if set(datapart[i][1:]) not in pointlist:
            pointlist.append(set(datapart[i][1:]))
          if set(datapart[i][1:]) ^ pointlist[j] not in pointlist:
            pointlist.append(set(datapart[i][1:]) ^ pointlist[j])
      ans.append(datapart[i][0])
  pointset = pointlist[0]
  for i in range(1, len(pointlist)):
    pointset = pointset | pointlist[i]
  l = len(pointset)
  while len(ans) >= l:
    del ans[-1]
  return ans

data = data.splitlines()
for i in range(1, len(data)):
  datapart = data[i]
  ans = findans(datapart)
  print(sum(ans))