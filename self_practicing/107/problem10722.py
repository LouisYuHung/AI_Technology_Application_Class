import sys
data = sys.stdin.read()
import random

def findanswer(datapart:str):
  datapart = datapart.split(',')
  order = int(datapart[-1])
  datatemp = datapart[1:-1]
  fac = 1
  i = int(datapart[0])
  while i != 0:
    fac *= i
    i -= 1
  anstemp = set({})
  while len(anstemp) < fac:
    random.shuffle(datatemp)
    anstemp.add(''.join(datatemp))
  anstemp = list(anstemp)
  anstemp.sort()
  print(anstemp[order - 1])
  
data =  data.splitlines()
for i in range(1, len(data)):
  findanswer(data[i])