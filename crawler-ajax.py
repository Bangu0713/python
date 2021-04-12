#抓取蝦皮，搜尋【口罩】的標題資料
import urllib.request as req
url="https://shopee.tw/api/v4/search/search_items?by=relevancy&keyword=%E5%8F%A3%E7%BD%A9&limit=20&newest=0&order=desc&page_type=search&version=2"
#建立一個 Request 物件，附加 Headers 的資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")   #根據觀察，取得的資料是JSON格式

#解析 JSON 格式的資料，取得每篇文章的標題
import json
data=json.loads(data)  #把原始的 JAON 資料解析成字典/列表的表現形式

titles=data["items"]
for key in titles:
    print(key["item_basic"]["name"])