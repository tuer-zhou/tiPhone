from fastapi import WebSocket

class WebSocketConnectionManager:
    def __init__(self) -> None:
        self.active_connections: list[WebSocket] = []
        self.dict_connctions: dict[int, WebSocket] = dict()

    async def accept_new_connection(self, ws: WebSocket):
        """
        Accepts new connection and adds it to the list of active connections
        """
        await ws.accept()
        self.active_connections.append(ws)

    async def map_connection_to_number(self, ws: WebSocket):
        json_data = await ws.receive_json()
        self.dict_connctions[json_data["src"]] = ws

    async def send_text_to_number(self, number: str, text: str):
        dst_ws = self.dict_connctions.get(number, None)
        if dst_ws:
            await dst_ws.send_text(f"{text}")

    def remove_connection(self, ws: WebSocket):
        self.active_connections.remove(ws)

    async def broadcast_msg(self, msg: str):
        for ws in self.active_connections:
            await ws.send_text(msg)
