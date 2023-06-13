from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import uvicorn


templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
@app.get("/index")
def index(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    
    