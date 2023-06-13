from fastapi import FastAPI
from fastapi.param_functions import Form
from starlette.requests import Request
from starlette.templating import Jinja2Templates
import uvicorn

from day13 import daomem
from day13.daomem import DaoMem


templates = Jinja2Templates(directory="templates")
app = FastAPI()

@app.get("/")
@app.get("/mem_list")
def mem_list(request:Request):
    de = DaoMem()
    list = de.selects()
    return templates.TemplateResponse("mem_list.html", {"request":request, "list":list})


@app.get("/mem_detail")
def mem_detail(request:Request, m_id:str):
    de = DaoMem()
    mem = de.select(m_id)

    return templates.TemplateResponse("mem_detail.html", {"request":request, "mem":mem})

@app.get("/mem_mod")
def mem_mod(request:Request, m_id:str):
    de = DaoMem()
    list = de.select(m_id)

    return templates.TemplateResponse("mem_mod.html", {"request":request, "list":list})

@app.post("/mem_mod_act")
def mem_mod_act(request:Request, m_id:str = Form(...), m_name:str=Form(...), tel:str=Form(...), email:str=Form(...)):
    de = DaoMem()
    cnt = de.update(m_id, m_name, tel, email)
    print("cnt",cnt)
    return templates.TemplateResponse("mem_mod_act.html", {"request":request, "cnt":cnt})

@app.get("/mem_add")
def mem_add(request:Request):
    return templates.TemplateResponse("mem_add.html", {"request":request})

@app.post("/mem_add_act")
def mem_add_act(request:Request, m_name:str=Form(...), tel:str=Form(...), email:str=Form(...)):
    de = DaoMem()
    cnt = de.insert(m_name, tel, email)
    print("cnt",cnt)
    return templates.TemplateResponse("mem_add_act.html", {"request":request, "cnt":cnt})

@app.post("/mem_del_act")
def mem_del_act(request:Request, m_id:str = Form(...)):
    de = DaoMem()
    cnt = de.delete(m_id)
    print("cnt",cnt)
    return templates.TemplateResponse("mem_del_act.html", {"request":request, "cnt":cnt})


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    
    