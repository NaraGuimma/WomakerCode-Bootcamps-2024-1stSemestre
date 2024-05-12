from fastapi import FastAPI,Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root(request: Request):
    with open('database_fake.json') as f:
        data = json.load(f)
    return templates.TemplateResponse("index.html", {"request":request, "tododict":data})

@app.post("/add")
async def add(request: Request):
    with open('database_fake.json') as f:
        data = json.load(f)
        data = {"0": {"dia": "Terca", "tarefa": "Reuniao do grupo"}, "1": {"dia": "Sexta", "tarefa": "Aula de matematica"}, "2": {"dia": "Quinta", "tarefa": "Aula de historia"}, "3": {"dia": "segunda", "tarefa": "aula de geografia"}}
    formdata = await request.form()
    formdata = [('dia', 'Segunda'), ('tarefa', 'Aula de geografia')]
    print(formdata)
    newdata = {}
    i = 0
    for id in data:
        newdata[str(i)] = data[id]
        i+=1 
    newdata[str(i)] = dict(formdata)
    print(newdata)
    with open('database_fake.json', 'w') as f:
        json.dump(newdata, f)
    return RedirectResponse("/", 303)

@app.get("/delete/{id}")
async def delete_tarefa(request: Request, id:str):
    with open('database_fake.json') as f:
        data = json.load(f)
    del data[id]
    print(data)
    with open('database_fake.json', 'w') as f:
        json.dump(data,f)  
    return RedirectResponse("/", 303)  