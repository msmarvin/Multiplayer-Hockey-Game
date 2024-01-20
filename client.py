import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"  # Sunucu IP'sini gerçek IP ile değiştirin

    async with websockets.connect(uri) as websocket:
        data_to_send = "Hello, server!"
        await websocket.send(data_to_send)
        print(f"Sent data: {data_to_send}")

        response = await websocket.recv()
        print(f"Server response: {response}")

asyncio.get_event_loop().run_until_complete(client())
