from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    """
    Retorna um item com o ID passado.
    """
    return {"item_id": item_id, "q": q}


