'''
[pre install]
pip3 install requests
pip3 install pyquery

sample input : 
2018/03/23 JPY 1000
2018/03/26 JPY 600
2018/04/25 EUR 120
2018/04/26 EUR 32
2018/05/02 USD 650
2018/05/03 USD 200

sample Output :
31288
'''

import requests
from pyquery import PyQuery as pq

total = 0
count = 0
while True:
    data= input()
    if (data == "0") or (data == '') or (count >= 10 ):
        break
    date = data.split(" ")[0]
    y = date.split("/")[0]
    m = date.split("/")[1]
    d = date.split("/")[2]
    currency = data.split(" ")[1]
    amount = data.split(" ")[2]

    dataUrl = 'https://rate.bot.com.tw/xrt/quote/' + y + '-' + m +'-' + d + '/' + currency + '/spot'
    doc = pq(url=dataUrl)
    fc = doc('tbody tr:last-child td:nth-child(6)').html()
    lc = round(float(fc) * float(amount))
    print(lc)
    total = total + lc
    count = count + 1
print(total)
