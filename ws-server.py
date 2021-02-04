import asyncio
import websockets
import json


async def run(websocket, path):
    json_str = await websocket.recv()
    data = json.loads(json_str)

    # debug print
    print(data['compiler'])
    print(data['std'])
    print(data['code'])
    ###

    code = data['code']

start_server = websockets.serve(run, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
