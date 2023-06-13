import pymysql



conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')

curs = conn.cursor()

e_id = "3" 
 

sql = f"""
    delete from emp
    where 
        e_id='{e_id}'
"""

curs.execute(sql)
print(curs.rowcount)
conn.commit()

curs.close()
conn.close()