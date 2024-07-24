import asyncio
import json

import websockets

from heartbeat import HeartBeat
from logger import Logger

#

# async def subscribe_orders(ws):
#     subscribe_message = {
#         "jsonrpc": "2.0",
#         "method": "private/subscribe",
#         "params": {
#             "channels": ["user.orders.BTC-PERPETUAL.raw"]  # Adjust the instrument as needed
#         },
#         "id": 1
#     }
#     await ws.send(json.dumps(subscribe_message))
#     print("Subscribed to orders")
#
# async def heartbeat(ws, interval=30):
#     while True:
#         await asyncio.sleep(interval)
#         ping_message = {
#             "jsonrpc": "2.0",
#             "method": "public/test",
#             "id": 2
#         }
#         await ws.send(json.dumps(ping_message))
#         print("Sent heartbeat")
#
# async def handle_messages(ws):
#     async for message in ws:
#         data = json.loads(message)
#         if "id" in data and data["id"] == 2:
#             print("Received heartbeat response")
#         elif "params" in data:
#             if "channel" in data["params"]:
#                 channel = data["params"]["channel"]
#                 if channel.startswith("user.orders"):
#                     print("Order update:", data["params"]["data"])
# #
# async def main():
#     uri = "wss://www.deribit.com/ws/api/v2"
#     async with websockets.connect(uri) as ws:
#         await subscribe_orders(ws)
#         await asyncio.gather(handle_messages(ws), heartbeat(ws))
#
# if __name__ == "__main__":
#     asyncio.run(main())


async def main():
    lger = Logger("main", log_file="./logs/main.log").get_logger()
    lger.info("Starting main")
    uri = "wss://www.deribit.com/ws/api/v2"
    async with websockets.connect(uri) as ws:
        lger.info("Connected to Deribit")
        await hb.start_heartbeat()
        lger.info("Started heartbeat")
        await asyncio.gather(hb.start_heartbeat(), hb.start_heartbeat())
        lger.info("Started heartbeat")
        # await subscribe_orders(ws)
        # await asyncio.gather(handle_messages(ws), heartbeat(ws))
        # await asyncio.gather(hb.start_heartbeat(), hb.start_heartbeat())
        # lger.info("Started heartbeat")
    hb = HeartBeat(interval=10)


if __name__ == "__main__":
    asyncio.run(main())
