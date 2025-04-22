import os
import json
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi import HTTPException

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/html", response_class=HTMLResponse)
def retornaHtml():
    caminho = "static/pagina.html"
    if os.path.exists(caminho):
        return FileResponse(caminho, media_type="text/html")

@app.get("/json", response_class=JSONResponse)
def retornaJson():
    caminho = "static/dados.json"
    if os.path.exists(caminho):
        with open(caminho, "r") as f:
            dados = json.load(f)
        return dados

@app.get("/imagem")
def retornaImagem():
    caminho = "static/image.png"
    if os.path.exists(caminho):
        return FileResponse(caminho, media_type="image/png")

@app.get("/js", response_class=PlainTextResponse)
def retornaJs():
    caminho = "static/script.js"
    if os.path.exists(caminho):
        with open(caminho, "r") as f:
            conteudo = f.read()
        return PlainTextResponse(content=conteudo, media_type="application/javascript")
    
@app.get("/pessoas", response_class=JSONResponse)
def listarPessoas():
    caminho = "static/dados.json"
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
        return dados
    return {"erro": "Arquivo de pessoas não encontrado"}

@app.post("/soma")
async def somar(request: Request):
    try:
        dados = await request.json()
        a = dados.get("a")
        b = dados.get("b")
        
        if a is None or b is None:
            raise HTTPException(status_code=400, detail="É necessário fornecer os dois números (a e b).")
        
        resultado = a + b
        return {"soma": resultado}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erro no envio dos dados ou na soma.")