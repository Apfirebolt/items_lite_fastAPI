from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()

# Initialize Jinja2Templates, pointing to your templates directory
templates = Jinja2Templates(directory="templates")

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

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


@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={"request": request}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

