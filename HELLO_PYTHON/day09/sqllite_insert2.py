import sqlite3
 
e_id = "5" 
e_name = "5" 
sex = "5" 
addr = "5" 
 
 
conn = sqlite3.connect("mydb.db")
 
cur = conn.cursor()

sql = """
    insert into emp
    (e_id, e_name, sex, addr) 
    values 
    (?,?,?,?)
"""
 
cur.execute(sql, ('4','4','4','4'))
print(cur.rowcount)
# commit 필수
conn.commit()
 
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close() 
conn.close()