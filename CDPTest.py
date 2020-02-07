import os
import asyncio
import websockets


async def hello():
    async with websockets.connect(uri) as ws:
        await ws.send(data)
        print(f"{data}")
        getting = await ws.recv()
        print(f"{getting}")

data = '''{
	"id": 1,
	"method": "Browser.getVersion"
}'''
uri = os.environ.get('URI')
print('websocket path is:', uri)

asyncio.get_event_loop().run_until_complete(hello())
