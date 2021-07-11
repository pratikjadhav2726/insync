import asyncio
import websockets

async def hello():
    uri = "ws://localhost:5003/ws"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        s=await websocket.recv()
        print(s)

asyncio.get_event_loop().run_until_complete(hello())