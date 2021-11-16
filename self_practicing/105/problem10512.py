import sys
data = sys.stdin.read()

data = data.splitlines()
dic = {"-----":0, ".----":1, "..---":2, "...--":3, "....-":4, ".....":5, "-....":6, "--...":7, "---..":8, "----.":9}

for i in range(1, len(data)):
  ans = []
  data[i] = data[i].split()
  for j in range(len(data[i])):
    ans.append(dic[data[i][j]])
  ans = [str(i) for i in ans]
  print("".join(ans))