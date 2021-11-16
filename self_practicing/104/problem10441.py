import sys
data = sys.stdin.read()


def devide(li):
  if len(li) > 1:
    Llist = []
    Rlist = []
    i = 1
    while i < len(li):
      if li[i] < li[0]:
        Llist.append(li[i])
      else:
        Rlist.append(li[i])
      i += 1
    li = [Llist] + [Rlist]
  else:
    pass
  return li
def findans(a:list):
  l = len(a)
  tree0 = [a[0]]
  tree1 = [-1, -1]
  tree2 = [-1, -1, -1, -1]
  tree3 = [-1, -1, -1, -1, -1, -1, -1, -1]
  for i in range(1, l):
    if a[i] < tree0[0] and tree1[0] == -1:
      tree1[0] = a[i]
    elif a[i] > tree0[0] and tree1[1] == -1:
      tree1[1] = a[i]
    elif a[i] < tree0[0] and a[i] < tree1[0] and tree2[0] == -1:
      tree2[0] = a[i]
    elif a[i] < tree0[0] and a[i] > tree1[0] and tree2[1] == -1:
      tree2[1] = a[i]
    elif a[i] > tree0[0] and a[i] < tree1[1] and tree2[2] == -1:
      tree2[2] = a[i]
    elif a[i] > tree0[0] and a[i] > tree1[1] and tree2[3] == -1:
      tree2[3] = a[i]
    elif a[i] < tree0[0] and a[i] < tree1[0] and a[i] < tree2[0] and tree3[0] == -1:
      tree3[0] = a[i]
    elif a[i] < tree0[0] and a[i] < tree1[0] and a[i] > tree2[0] and tree3[1] == -1:
      tree3[1] = a[i]
    elif a[i] < tree0[0] and a[i] > tree1[0] and a[i] < tree2[1] and tree3[2] == -1:
      tree3[2] = a[i]  
    elif a[i] < tree0[0] and a[i] > tree1[0] and a[i] > tree2[1] and tree3[3] == -1:
      tree3[3] = a[i]
    elif a[i] > tree0[0] and a[i] < tree1[1] and a[i] < tree2[2] and tree3[4] == -1:
      tree3[4] = a[i]
    elif a[i] > tree0[0] and a[i] < tree1[1] and a[i] > tree2[2] and tree3[5] == -1:
      tree3[5] = a[i]
    elif a[i] > tree0[0] and a[i] > tree1[1] and a[i] < tree2[3] and tree3[6] == -1:
      tree3[6] = a[i]
    elif a[i] > tree0[0] and a[i] > tree1[1] and a[i] > tree2[3] and tree3[7] == -1:
      tree3[7] = a[i]
    
  ans = [
    tree3[0], tree3[1], tree2[0],
    tree3[2], tree3[3], tree2[1], tree1[0],
    tree3[4], tree3[5], tree2[2],
    tree3[6], tree3[7], tree2[3], tree1[1], tree0[0]
  ]
  while -1 in ans:
    ans.remove(-1)
  return ans

data = data.splitlines()
while len(data) > 1:
  datapart = [int(i) for i in data[2].split(',')]
  li = devide(datapart)
  ansleft = []
  ansright = []
  if li[0] != []:  
    ansleft = findans(li[0])
  if li[1] != []:  
    ansright = findans(li[1])
  temp = ansleft + ansright + [datapart[0]]
  temp = [str(i) for i in temp]
  print(','.join(temp))
  del data[1:3]