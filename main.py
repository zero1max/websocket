import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict

app = FastAPI()


class ConnectionManager:
    """Foydalanuvchi ulanishlarini boshqaruvchi klass."""

    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, user_id: str):
        """Foydalanuvchini ulaydi va ro'yxatga qo'shadi."""
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: str):
        """Foydalanuvchini ro'yxatdan chiqaradi."""
        if user_id in self.active_connections:
            del self.active_connections[user_id]

    async def send_personal_message(self, message: str, to_user_id: str):
        """Bitta foydalanuvchiga xabar yuboradi."""
        websocket = self.active_connections.get(to_user_id)
        if websocket:
            await websocket.send_text(message)
        else:
            print(f"User {to_user_id} not connected.")

    async def broadcast(self, message: str):
        """Barcha foydalanuvchilarga xabar yuboradi."""
        for connection in self.active_connections.values():
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    """Har bir foydalanuvchi uchun WebSocket ulanish nuqtasi."""
    await manager.connect(websocket, user_id)
    await manager.broadcast(f"User {user_id} has joined the chat.")
    try:
        while True:
            data = await websocket.receive_json()
            message = data.get("message")
            to_user = data.get("to_user")

            if to_user:
                # Shaxsiy xabar yuborish
                await manager.send_personal_message(f"From {user_id}: {message}", to_user)
            else:
                # Xabarni hammaga yuborish
                await manager.broadcast(f"{user_id}: {message}")
    except WebSocketDisconnect:
        manager.disconnect(user_id)
        await manager.broadcast(f"User {user_id} has left the chat.")


if __name__ == "__main__":
    uvicorn.run( host="0.0.0.0", port=8000, reload=True)