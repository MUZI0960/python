import sqlite3

from fastapi import FastAPI
from fastapi.param_functions import Form
from sqlalchemy.ext.declarative import declarative_base
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
import uvicorn

from day09.sqllite_select import conn
from day12.daoemp import DaoEmp


templates = Jinja2Templates(directory="templates")
app = FastAPI()

@app.get("/")
@app.get("/emp_list")
def emp_list(request:Request):
    de = DaoEmp()
    list = de.selects()
    
    return templates.TemplateResponse("emp_list.html", {"request":request, "list":list})

@app.get("/emp_detail")
def emp_detail(request:Request, e_id:str):
    de = DaoEmp()
    list = de.select(e_id)

    return templates.TemplateResponse("emp_detail.html", {"request":request, "list":list})

@app.get("/emp_mod")
def emp_mod(request:Request, e_id:str):
    de = DaoEmp()
    list = de.select(e_id)

    return templates.TemplateResponse("emp_mod.html", {"request":request, "list":list})

@app.post("/emp_mod_act")
def emp_mod_act(request:Request, e_id:str = Form(...), e_name:str=Form(...), sex:str=Form(...), addr:str=Form(...)):
    de = DaoEmp()
    cnt = de.update(e_id, e_name, sex, addr)
    print("cnt",cnt)
    return templates.TemplateResponse("emp_mod_act.html", {"request":request, "cnt":cnt})

@app.get("/emp_add")
def emp_add(request:Request):
    return templates.TemplateResponse("emp_add.html", {"request":request})

@app.post("/emp_add_act")
def emp_add_act(request:Request, e_id:str = Form(...), e_name:str=Form(...), sex:str=Form(...), addr:str=Form(...)):
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, sex, addr)
    print("cnt",cnt)
    return templates.TemplateResponse("emp_add_act.html", {"request":request, "cnt":cnt})

@app.post("/emp_del_act")
def emp_del_act(request:Request, e_id:str = Form(...)):
    de = DaoEmp()
    cnt = de.delete(e_id)
    print("cnt",cnt)
    return templates.TemplateResponse("emp_del_act.html", {"request":request, "cnt":cnt})

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    
    