from fastapi import WebSocket

class WebSocketConnectionManager:
    def __init__(self) -> None:
        self.active_connections: list[WebSocket] = []

    async def accept_new_connection(self, ws: WebSocket):
        """
        Accepts new connection and adds it to the list of active connections
        """
        await ws.accept()
        self.active_connections.append(ws)

    async def remove_connection(self, ws: WebSocket):
        self.active_connections.remove(ws)

    async def broadcast_msg(self, msg: str):
        for ws in self.active_connections:
            await ws.send_text(msg)
