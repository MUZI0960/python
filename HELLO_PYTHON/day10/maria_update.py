import pymysql



conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')

curs = conn.cursor()

e_id = "3" 
e_name = "5" 
sex = "5" 
addr = "5"  

sql = f"""
    update emp 
    set
        e_name='{e_name}', sex='{sex}', addr='{addr}'
    where 
        e_id='{e_id}'
"""

curs.execute(sql)
print(curs.rowcount)
conn.commit()

curs.close()
conn.close()