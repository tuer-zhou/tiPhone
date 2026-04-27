from pydantic import BaseModel

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