import sys
arti = sys.stdin.read()
dlist = arti.split("\n")

ans = set(dlist[1].split(","))

for i in range(2, int(dlist[0])+2):
  dlist[i] = dlist[i].split(",")
  tlist = []
  count = [0, 0, 0, 0]
  for j in range(6):
    tlist = dlist[i][:j] + dlist[i][j+1:]
    tset = set(tlist)
    win = set({})
    for k in tlist:
      if k in ans:
        win.add(k)
    if len(win) == 2:
      count[0] = count[0] + 1
    elif len(win) == 3:
      count[1] = count[1] + 1
    elif len(win) == 4:
      count[2] = count[2] + 1
    elif len(win) == 5:
      count[3] = count[3] + 1
    else:
      continue
  count = [str(i) for i in count]
  print(",".join(count))