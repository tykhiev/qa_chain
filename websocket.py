import asyncio
import websockets

async def server(websocket, path):
    async for message in websocket: 
        await websocket.send(f'got your message: {message}')
        
start_server = websockets.server(server, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
