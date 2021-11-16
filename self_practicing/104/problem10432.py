import sys
data = sys.stdin.read()

def turned(temp):
  row = []
  for i in temp:
    i = i.split()
    i = [int(j) for j in i]
    row.append(i)
  return row

def find(matA, matB):
  matall = matA + matB
  pos = []
  # print(matall)
  i = 0
  while 9999 not in matall[i]:
    i += 1
  if i < len(matA):
    pos = ["A", i, matall[i].index(9999)]
  else:
    pos = ["B", i - len(matA), matall[i].index(9999)]
  return pos

def ans():
  diff = []
  if pos[0] == "A":
    tempAB = matAB[pos[1]]
    for i in range(csizeB):
      for j in range(csizeA):
        tempAB[i] -= matA[pos[1]][j] * matB[j][i]
      tempAB[i] += matA[pos[1]][pos[2]] * matB[pos[2]][i]
      diff.append(tempAB[i])
      if diff[i] != 0:
        diff[i] = int(diff[i] / matB[pos[2]][i])
    k = 0
    while diff[k] == 0:
      k += 1
    print(diff[k])
  else:
    tempAB = [matAB[i][pos[2]] for i in range(rsizeA)]
    for i in range(rsizeA):
      for j in range(rsizeB):
        tempAB[i] -= matA[i][j] * matB[j][pos[2]]
      tempAB[i] += matA[i][pos[1]] * matB[pos[1]][pos[2]]
      diff.append(tempAB[i])
      if diff[i] != 0:
        diff[i] = int(diff[i] / matA[i][pos[1]])
    k = 0
    while diff[k] == 0:
      k += 1
    print(diff[k])

data = data.splitlines()

while len(data) > 1:
  sizeAB = [int(i) for i in data[1].split(",")]
  rsizeA = sizeAB[0]
  rsizeB = sizeAB[2]
  csizeA = sizeAB[1]
  csizeB = sizeAB[3]
  datapart = data[1:2 + 2 * rsizeA + rsizeB]
  tempA = datapart[1:1 + rsizeA]
  tempB = datapart[1 + rsizeA:1 + rsizeA + rsizeB]
  tempAB = datapart[1+rsizeA+rsizeB:2+rsizeA+rsizeB+rsizeA]
  matA = turned(tempA)
  matB = turned(tempB)
  matAB = turned(tempAB)
  pos = find(matA, matB)
  ans()
  del data[1:2 + 2 * rsizeA + rsizeB]