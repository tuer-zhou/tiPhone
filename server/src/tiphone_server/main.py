from fastapi import FastAPI, WebSocket, WebSocketDisconnect


from .websocketsManager import WebSocketConnectionManager
from .dataTypes import AdvertisementMsg, AdvertisementResponse
app = FastAPI()

ws_manager = WebSocketConnectionManager()

all_ids = []
    

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

