from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import logging
import random
import json


from .websocketsManager import WebSocketConnectionManager
from .dataTypes import AdvertisementMsg, AdvertisementResponse

logger = logging.getLogger(__name__)
app = FastAPI()
origins = [
    "http://localhost:8000",
    "http://localhost:8001"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

ws_manager = WebSocketConnectionManager()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/advertisement")
async def advertisement(ad: AdvertisementMsg) -> AdvertisementResponse:
    """
    Updates alive status of client and creates phone number if not already done so
    """
    # TODO: read from real database
    logger.debug("got an advertisement")
    phone_number = "0100000" + str(random.randrange(0, 9))
    return {"phone_number": phone_number}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    Acts as a signaling server for the clients to exchange info to establish a WebRTC connection
    """
    await ws_manager.accept_new_connection(websocket)
    # TODO: might change to websocket only
    await ws_manager.map_connection_to_number(websocket)
    logger.debug("new websocket connection")
    try:
        while True:
            data = await websocket.receive_json()
            logger.debug(data)
            print(data)
            #print(ws_manager.dict_connctions)
            #await ws_manager.broadcast_msg(f"Message text was: {data}")
            dst_number = data.get("dst", None)
            if dst_number:
                await ws_manager.send_text_to_number(dst_number, json.dumps(data))

    except WebSocketDisconnect:
        logger.debug("websocket connection closed")
        ws_manager.remove_connection(websocket)
        await ws_manager.broadcast_msg("someone left")

