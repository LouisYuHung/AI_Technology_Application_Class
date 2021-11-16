import sys
data = sys.stdin.read()

def turned(temp):
  mat = []
  for i in temp:
    mat = mat + i.split()
  mat = [int(i) for i in mat]
  return mat
def testin(matA, matB):
  ii = "B"
  if 9999 in matA:
    ii = "A"
    ind = matA.index(9999)
    pr = ind // cA
    pc = ind % cA
  else:
    ind = matB.index(9999)
    pr = ind // cB
    pc = ind % cB
  return (ii, pr, pc)
def inpd(liA, liB):
  inn = 0
  for i in range(len(liA)):
    inn += liA[i] * liB[i]
  return inn
def ans():
  ansset = []
  if t[0] == "A":
    for i in range(cB):
      matab = matAB[i + cB * t[1]]
      wrong = matA[cA * t[1] + t[2]] * matB[i::cB][t[2]]
      tem = matab - inpd(matA[cA * t[1]:cA * (t[1] + 1)], matB[i::cB]) + wrong
      if tem != 0:
        tem = int(tem / matB[i::cB][t[2]])
      ansset.append(tem)
  else:
    for i in range(rA):
      matab = matAB[t[2]::cB][i]
      wrong = matA[cA * i + t[1]] * matB[t[2]::cB][t[1]]
      tem = matab - inpd(matA[cA * i:cA * (i + 1)], matB[t[2]::cB]) + wrong
      if tem != 0:
          tem = int(tem / matA[cA * i + t[1]])
      ansset.append(tem)
  return ansset

data = data.splitlines()

while len(data) > 1:
  temps = data[1]
  size = [int(i) for i in  temps.split(",")]  # [2, 3, 3, 4]
  rA = size[0]  # 2
  cA = size[1]  # 3
  rB = size[2]  # 3
  cB = size[3]  # 4
  datapart = data[1:2 + rA * 2 + rB]
  tempA = datapart[1:rA + 1]  # ["1 2 9999", "0 -4 1"]
  tempB = datapart[rA + 1:rA + rB + 1]  # ["3 1 0 2", "-1 2 5 0", "0 -2 2 1"]
  tempAB = datapart[rA + rB + 1:]   # ["1 -1 16 5", "4 -10 -18 1"]
  matA = turned(tempA)  # [1, 2, 9999, 0, -4, 1]
  matB = turned(tempB)  # [3, 1, 0, 2, -1, 2, 5, 0, 0, -2, 2, 1]
  matAB = turned(tempAB)  # [1, -1, 16, 5, 4, -10, -18, 1]
  t = testin(matA, matB)
  # print(matAB[(cB * t[1]) + 0])
  ansset = ans()
  j = 0
  while ansset[j] == 0:
    j += 1
    if j == len(ansset)-1:
      break
  print(ansset[j])
  del data[1:2 + rA * 2 + rB]