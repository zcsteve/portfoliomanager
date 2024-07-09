import pytest
from heartbeat import HeartBeat 
import websockets
import asyncio


class TestHeartbeat:
    async def test_heartbeat(self):
        async with websockets.connect('wss://test.deribit.com/ws/api/v2') as ws:
            heartbeat = HeartBeat(ws)
            await heartbeat.start_heartbeat()
            assert True
        pass

