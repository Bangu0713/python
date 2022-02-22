import pymysql
import charts1

# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "BETTY1998713",
    "db": "kkbox",
    "charset": "utf8"
}

try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
         # 新增資料SQL語法
         command = "REPLACE INTO charts(id, name, artist)VALUES(%s, %s, %s)"
         # 取得華語單曲日榜
         chartsD = charts1.get_charts_tracks("Gpohs15KF7KFktcN5B")
         for chart in chartsD:
             cursor.execute(
                 command, (chart["id"], chart["name"], chart["album"]["artist"]["name"]))
         # 儲存變更
         conn.commit()

except Exception as ex:
    print(ex)