from fastapi import FastAPI, WebSocket, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates=Jinja2Templates(directory="template")

@app.get("/")
def landing(request: Request):
    return templates.TemplateResponse(
        request,
        "route.html"
    )


@app.websocket("/ws/{name}")
async def websoc(
                websocket: WebSocket,
                 name:str):

    print("WEBSOCKET REQUEST RECEIVED")

    await websocket.accept()

    print("WEBSOCKET ACCEPTED")

    while True:
        message = await websocket.receive_text()

        print("MESSAGE:", message)
        print("client:", websocket.client)

        await websocket.send_text(message)


@app.get("/{name}")
def host_page(request: Request, name: str):
    return templates.TemplateResponse(
        request,
        "chat.html",
        {
            "username": name
        }
    )
