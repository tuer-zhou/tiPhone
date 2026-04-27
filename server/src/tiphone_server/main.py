from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from .websocketsManager import WebSocketConnectionManager

app = FastAPI()

ws_manager = WebSocketConnectionManager()

all_ids = []

class AdvertisementMsg(BaseModel):
    """
    Client sends this message when powered on, to indicate that they are reachable
    shared secret to ensure that client is part of the network. This secret is individual for each
    client
    """
    secret: str
    name: str

class AdvertisementResponse(BaseModel):
    """
    Response message to the Advertisement with phone number
    """
    phone_number: str

class SDP(BaseModel):
    """
    Session Description Protocol
    """
    # TODO: rework if necessary
    v: str
    o: str
    s: str
    c: str
    t: str
    m: str
    a: str
    

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    all_ids.append(item_id)
    return {"item_id": item_id, "q": q, "all": all_ids}

@app.post("/advertisement")
async def advertisement(ad: AdvertisementMsg) -> AdvertisementResponse:
    """
    Updates alive status of client and creates phone number if not already done so
    """
    # TODO
    return 

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    ws_manager.accept_new_connection(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            ws_manager.broadcast_msg(f"Message text was: {data}")
    except WebSocketDisconnect:
        ws_manager.remove_connection(websocket)
        ws_manager.broadcast_msg("someone left")

