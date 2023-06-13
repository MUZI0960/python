import pymysql


class DaoEmp:
    def __init__(self):
       self.conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')
       self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
       
    
    def selects(self):
        self.cur.execute("select * from emp")
        emps = self.cur.fetchall()
        return emps
    
    def select(self, e_id):
        sql = f"""
        select * from emp where e_id='{e_id}'
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        emp = None
        for e in rows:
            emp = e
        return emp
    
    def insert(self, e_id,e_name, sex, addr):
        sql = f"""
        insert into emp
        (e_id,e_name, sex, addr) 
        values 
        ('{e_id}','{e_name}','{sex}','{addr}')
        """ 
        self.cur.execute(sql)
        # commit 필수
        self.conn.commit()
        return self.cur.rowcount
    
    def update(self, e_id,e_name, sex, addr):
        sql = f"""
        update emp 
        set
            e_name='{e_name}', sex='{sex}', addr='{addr}'
        where 
            e_id='{e_id}'
        """
        self.cur.execute(sql)
        self.conn.commit()
    
    def delete(self, e_id):
        sql = f"""
        delete from emp
        where 
            e_id='{e_id}'
        """ 
        self.cur.execute(sql)
        self.conn.commit()
        
        return self.cur.rowcount
    
        
    def __del__(self):
        self.cur.close()  
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    # list = de.selects()
    
    # cnt = de.insert("4", "4", "4","4")
    cnt = de.delete("4")
    # cnt = de.update("1", "9", "9", "9")
    # emp = de.select("1")    
    print(cnt)
    
    
    
    
    
    
    
    
    