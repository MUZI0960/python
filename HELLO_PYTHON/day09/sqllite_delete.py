import sqlite3

e_id = "3" 

 
conn = sqlite3.connect("mydb.db")
 
cur = conn.cursor()

sql = f"""
    delete from emp
    where 
        e_id='{e_id}'
"""
 
cur.execute(sql)
# commit 필수
conn.commit()
 
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close() 
conn.close()