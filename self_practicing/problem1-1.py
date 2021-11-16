import sys
def findnum(str_a):
  def cut(str):
    i = 0
    if len(str) != 0:
      str = str + "0"
      while int(str[i]) <= int(str[i+1]):
        i += 1
      else:
        i = i+1
        str = str[:-1]
      str = str[i:]
    else:
      str = str
    return str, i
  textlist = []
  numlist = [0]
  tup = ("",1)
  while tup[1] != 0:
    tup = cut(str_a)
    if tup[1] != 0: 
      textlist.append(tup[0])
      numlist.append(tup[1])
      str_a = tup[0]
  print(max(numlist))

arti = sys.stdin.read()
table = arti.split("\n")
for i in table:
  findnum(i)