from fastapi import FastAPI, WebSocket, Request, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from model import User

app = FastAPI()
templates=Jinja2Templates(directory="template")
user_obj_list=[

]


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
    user=User(name,websocket)
    user_obj_list.append(
        user
    )
    print("WEBSOCKET ACCEPTED")

    try:
        while True:
            message = await websocket.receive_json()
            target=message["to"]
            msg=message["message"]
            type=message["type"]
            

            for user in user_obj_list:
                if user.username==target:
                    await user.send_message(
                        {
                            "to":target,
                            "from":name,
                            "message":msg,
                            "type":type
                        }
                    )

            
    except WebSocketDisconnect:
        user_obj_list.remove(user)


@app.get("/{name}")
def host_page(request: Request, name: str):
    return templates.TemplateResponse(
        request,
        "chat.html",
        {
            "username": name
        }
    )


@app.get("/ws/connections")
def avail_connections():

    users=[x.username for x in user_obj_list]

    return users