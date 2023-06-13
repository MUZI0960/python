import sqlite3

from fastapi import FastAPI
from fastapi.param_functions import Form
from sqlalchemy.ext.declarative import declarative_base
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
import uvicorn

from day09.sqllite_select import conn


templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return "Hello World"

@app.get("/para", response_class=HTMLResponse)
async def para(a:str):
    return "para:" + str(a)

@app.post("/post", response_class=HTMLResponse)
async def post(a:str=Form(...)):
    return "Hello post" + a

@app.get("/forw",  response_class=HTMLResponse)
def forw(request:Request):
    a = "홍길동"
    arr = ["서혜정", "유관순", "아이유", "카리나"]
    mylist = [
        {"e_id":"1", "e_name":"1", "sex":"1", "addr":"1"},
        {"e_id":"2", "e_name":"2", "sex":"2", "addr":"2"},
        {"e_id":"3", "e_name":"3", "sex":"3", "addr":"3"}
        ] 
    return templates.TemplateResponse("forw.html", {"request":request, "a":a, "arr":arr, "mylist":mylist})

Base = declarative_base()
dsn = "sqlite://db.sqlite"

@app.get("/emp")
def emp(request:Request):
    mylist = []
    conn = sqlite3.connect("mydb.db")
    cur = conn.cursor()
    cur.execute("select * from emp")
     
    rows = cur.fetchall()
    for e in rows:
        print(e)
        mylist.append({"e_id":e[0],"e_name":e[1],"sex":e[2],"addr":e[3]})

    cur.close() 
    conn.close()
    
    return templates.TemplateResponse("emp.html", {"request":request, "mylist":mylist})

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    
    