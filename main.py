from fastapi import FastAPI
import uvicorn
import json
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.get("/users")
def read_users():
    users = [{
        "id": 1,
        "name": "Alice"
    }, {
        "id": 2,
        "name": "Bob"
    }]
    return JSONResponse(content=users)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

