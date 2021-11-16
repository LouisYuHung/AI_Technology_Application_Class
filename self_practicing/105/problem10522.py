import sys
data = sys.stdin.read()

def findfactor(num:int):
  factor = set({})
  i = 1
  while i <= num:
    if num % i == 0:
      factor.add(i)
    i += 1
  return factor

def findanswer(datapart:str):
  datapart = datapart.split(',')
  datapart = [int(i) for i in datapart]
  ansset = []
  for i in range(len(datapart)):
    for j in range(i + 1, len(datapart)):
      ansset.append(findfactor(datapart[i]) & findfactor(datapart[j]))
  for i in range(len(ansset)):
    ansset[i] = max(ansset[i])
  print(max(ansset))

data = data.splitlines()
for i in data[1:]:
  findanswer(i)