''' 
sample input : 
2018/5/1
5
AB 5/1
BC 1/20
CD 10/10
DE 7/8
EF 2/28

sample Output :
AB 0 days
DE 68 days
CD 162 days
BC 264 days
EF 303 days
''' 

import datetime

birthdayList={}

today = input("Insert Today [yyyy/mm/dd]:")
tYear = int(today.split("/")[0])
tMonth = int(today.split("/")[1])
tDay = int(today.split("/")[2])
tDate = datetime.datetime(tYear,tMonth, tDay)
tDayGap = tDate.timestamp()


member_num = int(input("Insert member Number: "))


i = 0
while i < member_num:
  memberList = input("Insert Name & Birthday:")  
  name = memberList.split(" ")[0]
  birthday = memberList.split(" ")[1]

  bM = int(birthday.split("/")[0])
  bD = int(birthday.split("/")[1])
  setDate = datetime.datetime(tYear,bM, bD)
  dayGap = setDate.timestamp()
  if dayGap < tDayGap:
    setDate = datetime.datetime(tYear+1,bM, bD)
    dayGap = setDate.timestamp()
  
  total = int(abs((tDayGap - dayGap) / 86400))

  birthdayList[name] = total
  
  member_num -= 1 

for s in sorted(birthdayList, key=birthdayList.get):
  print(s, ' ', birthdayList[s], 'days')