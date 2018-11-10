''' 
sample input : 
are 2
today 4
How 1
you 3
0
sample Output :
How are you today.
Taipai
''' 

resultlist={}
while True:
    str1= input("Please enter two digits separated by space : ")
    if str1 == "0":
        break
    strtext = str1.split(" ")[0]
    location = int(str1.split(" ")[1])
    resultlist[location] = strtext

#print (resultlist)

lista = []
for s in sorted(resultlist):
   lista.append(resultlist[s])

#lista.append('.')
result = " ".join(lista) + '.'
print (result)