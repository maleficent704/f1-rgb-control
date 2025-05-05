# main.py

import asyncio
import websockets
import json
from config import F1MV_HOST, F1MV_PORT
from nanoleaf import flash_color, cycle_rainbow

F1MV_WS_URL = f"ws://{F1MV_HOST}:{F1MV_PORT}/graphql"

GRAPHQL_SUBSCRIPTION = {
    "type": "start",
    "id": "1",
    "payload": {
        "query": """
        subscription {
            TrackStatus {
                Status
                Message
            }
        }
        """,
        "variables": {}
    }
}

async def listen_for_events():
    async with websockets.connect(F1MV_WS_URL) as websocket:
        await websocket.send(json.dumps({"type": "connection_init"}))
        await websocket.send(json.dumps(GRAPHQL_SUBSCRIPTION))

        print("Listening for events...")
        while True:
            try:
                response = await websocket.recv()
                data = json.loads(response)

                if data.get("type") == "data":
                    track_status = data["payload"]["data"]["TrackStatus"]
                    status = track_status["Status"]
                    message = track_status["Message"]

                    print(f"Track Status: {message} (Code: {status})")

                    if status == "2":
                        print("Yellow flag! Flashing yellow.")
                        flash_color(hue=60)
                    elif status == "4":
                        print("Red flag! Flashing red.")
                        flash_color(hue=0)
                    elif status == "1":
                        print("Green flag! Rainbow cycle!")
                        cycle_rainbow()

            except Exception as e:
                print(f"WebSocket error: {e}")
                break

asyncio.run(listen_for_events())