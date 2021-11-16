# import sys
# arti = sys.stdin.read()
# dlist = arti.split("\n")
# 同花順: 7, 鐵支: 6*, 葫蘆: 5*, 順子: 4, 三條: 3*, 兩對: 2*, 一對: 1*, 雜牌: 0*
dlist = "14 16 18 19 20 21"
def colorjudge(H):
  color = []
  for i in range(5):
    if H[i] - 39 > 0:
      s_type = 4
    elif H[i] - 26 > 0:
      s_type = 3
    elif H[i] - 13 > 0:
      s_type = 2
    else:
      s_type = 1
    color.append(s_type)
  return color
def pointjudge(H,color):
  p_test = []
  for i in range(5):
    p_test.append(H[i] - color[i]*13 + 13)
  p_test = sorted(p_test)
  p0 = p_test.count(p_test[-1])
  if len(set(p_test)) == 2:
    if p0 == 1 or p0 == 4:
      # print("鐵支 6")
      ppp = 6
    else:
      # print("葫蘆 5")
      ppp = 5
  elif len(set(p_test)) == 3:
    if p0 == 3:
      # print("三條 3")
      ppp = 3
    elif p0 == 2:
      # print("兩對 2")
      ppp = 2
    elif p0 == 1:
      p_test = p_test[:4]
      p0 = p_test.count(p_test[-1])
      if p0 == 3:
        # print("三條 3")
        ppp = 3
  elif len(set(p_test)) == 4:
    # print("一對 1")
    ppp = 1
  else:
    if p_test[-1] - p_test[0] == 4 or p_test[1] - p_test[0] == 9:
      if len(set(color)) == 1:
        # print("同花順 7")
        ppp = 7
      else:
        # print("順子 4")
        ppp = 4
    else:
      # print("雜牌 0")
      ppp = 1    
  return ppp
def runall(list_h):
  result = []
  for i in range(6):
    list_test = list_h[:i]+list_h[i+1:]
    color = colorjudge(list_test)
    result.append(pointjudge(list_test, color))
  print(max(result))

for i in range(int(dlist[0])):
  hand = dlist[i+1].split()
  hand = sorted([int(i) for i in hand])
  runall(hand)