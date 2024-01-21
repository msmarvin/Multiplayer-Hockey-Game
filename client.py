import asyncio
import websockets

name = "player1"


async def client(location, degree, ball_speed, color):
    uri = "ws://localhost:8765"  # Sunucu IP'sini gerçek IP ile değiştirin

    try:
        async with websockets.connect(uri) as websocket:
            data_to_send = name + "|" + str(location) + " |" + str(degree) + "|" + str(ball_speed) + "|" + str(color)
            await websocket.send(data_to_send)
            print(f"Sent data: {data_to_send}")
            response = await websocket.recv()
            print(f"Server response: {response}")
    except websockets.exceptions.ConnectionClosedOK:
        print("Websocket connection closed")


