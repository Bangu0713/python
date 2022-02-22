import requests
# 取得Token
def get_access_token():
    #API網址    
    url = "https://account.kkbox.com/oauth2/token" 
    
    #標頭
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "account.kkbox.com"
    }
    
    #參數
    data = {
        "grant_type": "client_credentials",
        "client_id": "15e6f180eeeaae0ba8b6bd0c704f87db",
        "client_secret": "67db81dad466333fcfb2f4cb82653a5c"
    }
    access_token = requests.post(url, headers=headers, data=data)
    return access_token.json()["access_token"]

# 取得各種音樂排行榜列表
def get_charts():
    #取得存取憑證
    access_token = get_access_token() 
   #取得音樂排行榜列表API網址
    url = "https://api.kkbox.com/v1.1/charts"
    #標頭
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + access_token  #帶著存取憑證
    }
    #參數
    params = {
        "territory": "TW"  #台灣領域  
    }
    response = requests.get(url, headers=headers, params=params)
    result = response.json()["data"]
    for item in result:
        print(item["id"], item["title"])
get_charts() 
 
# 取得該音樂排行榜的歌曲列表
def get_charts_tracks(chart_id):
    #存取憑證
    access_token = get_access_token() 
    #取得音樂排行榜列表中的歌曲API網址
    url = "https://api.kkbox.com/v1.1/charts/" + chart_id + "/tracks"
    #標頭
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + access_token
    }
    #參數
    params = {
        "territory": "TW"  #台灣領域
    }
    response = requests.get(url, headers=headers, params=params)
    result = response.json()["data"]
    for item in result:
        print([item["name"], item["url"]])
    return result 

print("===========================================")
try:
    chart_id = input("請貼上想聽的音樂排行榜ID: ")
    get_charts_tracks(chart_id)
except KeyError:
    print("請貼上正確的音樂排行榜ID")