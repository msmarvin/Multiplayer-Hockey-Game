import asyncio
import websockets

socket = None

async def server(websocket):
    data = await websocket.recv()
    name, location, degree, ball_speed, color = data.split("|")
    data = f"Name: {name}, Degree: {degree}, Speed: {ball_speed}, Color: {color}"
    print(data)


async def main():
    async with websockets.serve(server,  "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
