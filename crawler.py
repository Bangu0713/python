#抓取PTT電影版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立一個 Request 物件，附加 Headers 的資訊
request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

#解析原始碼，取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser")  # 讓 BeautifulSoup 協助我們解析 HTML 的文件
titles=root.find_all("div",class_="title")  # 尋找所有 class="title" 的 div 標籤
for title in titles:
    if title.a != None:   # 如果標題包含 a 標籤 (沒有被刪除)，印出來
        print(title.a.string)