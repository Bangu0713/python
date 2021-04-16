import pymysql
import csv
import codecs
import urllib.request as req
import bs4
import re

conn = pymysql.connect(
        host='localhost', 
        port=3306, 
        user='root', 
        passwd='BETTY1998713', 
        db='bank', 
        charset='utf8'
)

url="https://rate.bot.com.tw/xrt?Lang=zh-TW"

request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser") 
titles=root.find_all("div","hidden-phone print_show")  
data1=root.find_all("td","rate-content-cash text-right print_hide")
data2=root.find_all("td","rate-content-sight text-right print_hide")
for n in range(0,len(titles)):
    currency=titles[n].text.strip()
    cash_in=data1[n*2].text.strip()
    cash_out=data1[n*2+1].text.strip()
    sight_in=data2[n*2].text.strip()
    sight_out=data2[n*2+1].text.strip()
    try:    
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO stock (currency,cash_in,cash_out,sight_in,sight_out) VALUES (%s,%s,%s,%s,%s)',(currency,cash_in,cash_out,sight_in,sight_out))
            conn.commit()
    except Exception as ex:
        print(ex)

