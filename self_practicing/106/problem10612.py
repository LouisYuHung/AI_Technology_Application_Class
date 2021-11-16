data = '''8
MCDXXXVII
XCIX
CXCIX
DCCLXIV
CCLXVIII
MMMCC
DCCVII
MMCDLXIX'''

def testnum(num:str):
  if len(num) < 3:
    temp = [num]
  else:
    temp = []
    for i in range(len(num)):
      if num[i] == 'M':
        if num[i-1] == 'C' and i - 1 >= 0:
          temp.append('CM')
        else:
          temp.append('M')
    num = num.replace('CM','')
    num = num.replace('M', '')
    if num[0] == 'C' and num[1] == 'D':
      temp.append('CD')
      num = num.replace('CD','')
    elif num[0] == 'D':
      temp.append('D')
      num = num.replace('D', '')
    for i in range(len(num)):
      if num[i] == 'C':
        if num[i-1] == 'X' and i - 1 >= 0:
          temp.append('XC')
        else:
          temp.append('C')
    num = num.replace('XC','')
    num = num.replace('C', '')
    if num != '':
      if num[0] == 'X' and num[1] == 'L':
        temp.append('XL')
        num = num.replace('XL','')
      elif num[0] == 'L':
        temp.append('L')
        num = num.replace('L', '')
      for i in range(len(num)):
        if num[i] == 'X':
          if num[i-1] == 'I' and i - 1 >= 0:
            temp.append('IX')
          else:
            temp.append('X')
      num = num.replace('IX', '')
      num = num.replace('X', '')
      if num != '':
        if num[0] == 'I' and num[1] == 'V':
          temp.append('IV')
          num = num.replace('IV','')
        elif num[0] == 'V':
          temp.append('V')
          num = num.replace('V', '')
        for i in range(len(num)):
          if num[i] == 'I':
            temp.append('I')
        num = num.replace('I', '')
  return temp

value = {
  'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 
  'II':2, 'IV':4, 'VI':6, 'IX':9, 'XI':11, 'XV':15, 
  'XX':20, 'XL':40, 'LX':60, 'XC':90, 'CX':110, 'CL':150,
  'CC':200, 'CD':400, 'DC':600, 'CM':900, 'MC':1100, 'MD':1500}
data = data.splitlines()
for i in range(1, len(data)):
  datalist = testnum(data[i])
  for j in range(len(datalist)):
    datalist[j] = value[datalist[j]]
  print(sum(datalist))