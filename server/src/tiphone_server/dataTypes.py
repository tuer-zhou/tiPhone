from pydantic import BaseModel
from typing import Literal

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

class WebSocketMsg(BaseModel):
    msg_type: Literal["INIT", "CALL_REQUEST", "CALL_END", "CALL_CANCEL", "CALL_ACCEPT", "ICE_EXCHANGE"]
    src: str
    dst: str

class WebSocketInit(BaseModel):
    msg_type: Literal["INIT"]
    secret: str
    src: str

class CallRequest(WebSocketMsg):
    sdp_offer: str

class CallEnd(WebSocketMsg):
    pass

class CallCancel(WebSocketMsg):
    pass

class CallAccept(WebSocketMsg):
    sdp_answer: str

class ICEExchagne(WebSocketMsg):
    ice_data: str

