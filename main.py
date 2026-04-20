from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")  #endpoint punto dove chiamiamo il nostro server web
def home():
    return FileResponse('static/index.html')