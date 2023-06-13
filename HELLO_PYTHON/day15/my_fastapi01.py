from typing import Optional

from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic.main import BaseModel
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse
import uvicorn

from day15 import DaoEmp


templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

class Emp(BaseModel):
    e_id: Optional[str] =None
    e_name: Optional[str] =None
    sex : Optional[str] =None
    addr: Optional[str] =None

@app.get("/")
@app.get("/index")
async def index(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/myajax")
async def myajax(emp : Emp):
    print(emp)
    json ={
        'name': '홍길동'
    }        
    return JSONResponse(json)

@app.post("/myajax_selects")
async def myajax_selects():
    de = DaoEmp()
    json = de.selects()    
    return JSONResponse(json)
 
@app.post("/myajax_select")
async def myajax_select(emp:Emp):
    de = DaoEmp()
    json = de.select(emp.e_id)  
    return JSONResponse(json)

@app.post("/myajax_insert")
async def myajax_insert(emp:Emp):
    de = DaoEmp()
    json = de.insert(emp.e_id, emp.e_name, emp.sex, emp.addr)
    return JSONResponse(json)

@app.post("/myajax_update")
async def myajax_update(emp:Emp):
    de = DaoEmp()
    json = de.update(emp.e_id, emp.e_name, emp.sex, emp.addr)
    return JSONResponse(json)


@app.post("/myajax_delete")
async def myajax_delete(emp:Emp):
    de = DaoEmp()
    json = de.delete(emp.e_id)
    return JSONResponse(json)
 
 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)











