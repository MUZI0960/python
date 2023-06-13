import sqlite3

e_id = "3" 
e_name = "9" 
sex = "9" 
addr = "9"  
 
conn = sqlite3.connect("mydb.db")
 
cur = conn.cursor()

sql = f"""
    update emp 
    set
        e_name='{e_name}', sex='{sex}', addr='{addr}'
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