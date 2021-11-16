import sys
data = sys.stdin.read()
# data = '''3
# This is a sample file.
# Hello World!!
# SOS!'''

data = data.splitlines()
for i in range(1, len(data)):
  datapart = data[i].split(" ")
  count = 0
  for i in datapart:
    if 's' in i or 'S' in i:
      count += 1
  print(str(len(datapart)) + ',' + str(count))