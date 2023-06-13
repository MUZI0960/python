import pymysql



conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')

curs = conn.cursor()

e_id = "3" 
e_name = "3" 
sex = "3" 
addr = "3"  

sql = f"""
    insert into emp
    (e_id, e_name, sex, addr) 
    values 
    ('{e_id}','{e_name}','{sex}','{addr}')
"""

curs.execute(sql)
print(curs.rowcount)
conn.commit()

curs.close()
conn.close()

