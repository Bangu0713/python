import pymysql
import charts

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
    #     # 新增資料SQL語法
    #     command = "INSERT INTO charts(id, name, artist)VALUES(%s, %s, %s)"
    #     # 取得華語單曲日榜
    #     charts = charts.get_charts_tracks("LYbUM8vIUkVZz1ov_l")
    #     for chart in charts:
    #         cursor.execute(
    #             command, (chart["id"], chart["name"], chart["album"]["artist"]["name"]))
    #     # 儲存變更
    #     conn.commit()
    #   #資料表相關操作
        # 新增資料指令
        command = "SELECT * FROM charts WHERE name = %s"
        # 執行指令
        cursor.execute(command, ("太陽",))
        # 取得所有資料
        result = cursor.fetchall()
        print(result)
except Exception as ex:
    print(ex)