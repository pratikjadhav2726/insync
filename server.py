import asyncio
import websockets

async def echo(websocket, path):
    s=await websocket.recv()
    print(s)
    
    await websocket.send("Your reply")

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()