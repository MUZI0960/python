import sqlite3
from hamcrest.core.core.isnone import none

class DaoEmp:
    def __init__(self):
       self.conn = sqlite3.connect("mydb.db")
       self.cur = self.conn.cursor()
       
    
    def selects(self):
        emps = []
        self.cur.execute("select * from emp")
        rows = self.cur.fetchall()
        for e in rows:
            emps.append({"e_id":e[0],"e_name":e[1],"sex":e[2],"addr":e[3]})
        
        return emps
    
    def insert(self, e_id, e_name, sex, addr):
        sql = f"""
        insert into emp
        (e_id, e_name, sex, addr) 
        values 
        ('{e_id}','{e_name}','{sex}','{addr}')
        """ 
        self.cur.execute(sql)
        # commit 필수
        self.conn.commit()
        return self.cur.rowcount
    
    def update(self, e_id, e_name, sex, addr):
        sql = f"""
        update emp 
        set
            e_name='{e_name}', sex='{sex}', addr='{addr}'
        where 
            e_id='{e_id}'
        """
        self.cur.execute(sql)
        self.conn.commit()
        
        return self.cur.rowcount
        
    def delete(self, e_id):
        sql = f"""
        delete from emp
        where 
            e_id='{e_id}'
        """ 
        self.cur.execute(sql)
        self.conn.commit()
        
        return self.cur.rowcount
    
    def select(self, e_id):
        sql = f"""
        
        select * from emp where e_id='{e_id}'
        
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        emp = None
        for e in rows:
            emp = e
        return {"e_id":e[0],"e_name":e[1],"sex":e[2],"addr":e[3]}
    
    # select(e_id)
    # update(e_id, e_name,sex,addr):
    
    # delete(e_id)
        
        
    def __del__(self):
        self.cur.close() 
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    
    # cnt = de.selects()
    
    cnt = de.update("3", "9", "9", "9")
    # emp = de.select("3")    
    print(cnt)
    
    
    
    
    
    
    
    
    