''' 
sample input : 
Taipai 16
London 41

sample Output :
Taipai
''' 


print('請輸入 地區A  國家, 溫度(攝氏C)')
areaA = input()
c1 = areaA.split(',')[0]
t1 = float(areaA.split(',')[1])

print('請輸入 地區B  國家, 溫度(華氏F)')
areaB = input()
c2 = areaB.split(',')[0]
t2 = float(areaB.split(',')[1])

t2 = 5/9*(t2-32)

if t1 > t2:
  print(c1)
elif t1 < t2:
  print(c2)
else:
  print('溫度一樣')    

##print(c1)
##print(t1)