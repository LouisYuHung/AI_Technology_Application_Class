import sys
arti = sys.stdin.read()
dlist = arti.splitlines()


def judge(olist):
  li = sorted([int(i) % 13 for i in olist])
  sli = set(li)
  point = 0
  if len(sli) == 2:
    if li.count(li[0]) == 1 or li.count(li[0]) == 4:
      # print("鐵支 6")
      point = 6
    else:
      # print("葫蘆 5")
      point = 5
  elif len(sli) == 3:
    for i in sli:
      if li.count(i) == 3:
        # print("三條 3")
        point = 3
    if point != 3:
      # print("兩對 2")
      point = 2
      
  elif len(sli) == 4:
    # print("一對 1")
    point = 1
  else:
    straight = [[i, i+1, i+2, i+3, i+4] for i in range(1,9)] + [[0, 9, 10, 11, 12]] + [[0, 1, 10, 11, 12]]
    if li in straight:
      if len(colortest(olist)) == 1:
        # print("同花順 7")
        point = 7
      else:
        # print("順子 4")
        point = 4
    else:
      # print("雜牌 0")
      pass
  return point

def colortest(li):
  clist = []
  for i in li:
    if i > 39:
      clist.append("c")
    elif i > 26:
      clist.append("d")
    elif i > 13:
      clist.append("h")
    else:
      clist.append("s")
  return set(clist)

for j in range(1, len(dlist)):
  set1 = dlist[j].split()
  set1 = [int(i) for i in set1]
  num = set({})
  for i in range(6):
    temp = set1[:i] + set1[i + 1:]
    ppp = judge(temp)
    num.add(ppp)
  print(max(num))