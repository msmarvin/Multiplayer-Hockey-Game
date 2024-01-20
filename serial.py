import asyncio
import websockets


async def server(websocket, path):
    try:
        while True:
            data = await websocket.recv()
            print(f"Received data: {data}")
            await websocket.send(f"Server received: {input('enter daha: ')}")
    except websockets.exceptions.ConnectionClosedOK:
        pass
    except websockets.exceptions.ConnectionClosedError as e:
        pass

start_server = websockets.serve(server, "0.0.0.0", 8765)

asyncio.run(start_server)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()
