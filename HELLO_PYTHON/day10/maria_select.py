import pymysql


conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')

sql = "SELECT * FROM emp"

with conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        result = cur.fetchall()
        for data in result:
            print(data)