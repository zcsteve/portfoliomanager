import asyncio
import json
from dataclasses import dataclass

from websockets import WebSocketClientProtocol


@dataclass
class HeartBeat:

    ws: WebSocketClientProtocol
    interval: int = 10

    async def start_heartbeat(self):
        start_heartbeat_message = {
            "jsonrpc": "2.0",
            "id": 9098,
            "method": "public/set_heartbeat",
            "params": {"interval": self.interval},
        }
        await self.ws.send(json.dumps(start_heartbeat_message))
        response = await self.ws.recv()
        response = json.loads(response)
        if response.get("result") != "ok":
            raise Exception("Failed to start heartbeat")

        while True:
            await asyncio.sleep(self.interval)
            ping_message = {"jsonrpc": "2.0", "method": "public/test", "id": 2}
            await self.ws.send(json.dumps(ping_message))
            print("Sent heartbeat")
