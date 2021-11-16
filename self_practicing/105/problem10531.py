data = '''3
4,8,6,1,10,16,5,14,13
1,4,5,6,8,10,13,14,16
4,8,6,10'''
data = data.splitlines()
for i in range(1, len(data)):
  data[i] = data[i].split(',')
print(data)