from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd

app = FastAPI()
df = pd.read_excel("/workspaces/PAGINA_LOGIN/dati.xlsx")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/") # Endpoint: punto in cui andiamo a richiamare il server web
def home():
    # Restituisce direttamente il file HTML
    return FileResponse('static/index.html')

@app.post("/login")
def Controlla(username: str = Form(...), password: str = Form(...)):
    if username.lower() == "admin" and password == "xxx123##":
        return {"messaggio": 1}
    else:
        return {"messaggio": 0}

@app.post("/login2")
def Controlla(username: str = Form(...), password: str = Form(...)):
    if username.lower() == "admin" and password == "xxx123##":
        return {"messaggio": 1}
    else:
        return {"messaggio": 0}

@app.post("/loginPandas")
def ControllaPassword(username: str = Form(...), password: str = Form(...)):
    risultato = df[(df["USER"]==username) & (df["NAME"]== password)]
    if not risultato.empty :
        return {"messaggio": 1}
    else:
        return {"messaggio" : 0}