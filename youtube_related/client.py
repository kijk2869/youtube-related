import asyncio
import json
import re
from collections import deque
from typing import Deque, Dict, List, Match, Pattern

import aiohttp

from .error import RateLimited

headers: dict = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
}

DATA_JSON: Pattern = re.compile(
    r'(?:window\["ytInitialData"\]|ytInitialData)\W?=\W?({.*?});'
)


def fetch(vURL: str, local_addr: str = None) -> List[Dict]:
    return asyncio.run(async_fetch(vURL, local_addr))


async def async_fetch(vURL: str, local_addr: str = None) -> List[Dict]:
    connector: aiohttp.TCPConnector = (
        aiohttp.TCPConnector(local_addr=(local_addr, 0)) if local_addr else None
    )
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        async with session.get(vURL) as response:
            if response.status == 429:
                raise RateLimited

            RAW: str = await response.text()

    Search: Match = DATA_JSON.search(RAW)

    if not Search:
        raise ValueError("Could not extract ytInitialData.")

    Data: Dict = json.loads(Search.group(1))

    Overlay: Dict = Data["playerOverlays"]["playerOverlayRenderer"]
    watchNextEndScreenRenderer: Dict = Overlay["endScreen"][
        "watchNextEndScreenRenderer"
    ]
    Result: list = [
        {
            "id": Item["videoId"],
            "title": Item["title"]["simpleText"],
            "duration": Item["lengthInSeconds"] if "lengthInSeconds" in Item else None,
        }
        for Item in [
            result["endScreenVideoRenderer"]
            for result in watchNextEndScreenRenderer["results"]
            if "endScreenVideoRenderer" in result
        ]
    ]

    return Result


class preventDuplication:
    def __init__(self):
        self._LastRelated: Deque = deque(maxlen=10)

    def get(self, vURL: str, local_addr: str = None) -> Dict:
        return asyncio.run(self.async_get(vURL, local_addr))

    async def async_get(self, vURL: str, local_addr: str = None) -> Dict:
        Data: List[Dict] = await async_fetch(vURL, local_addr)

        for Item in Data:
            if not Item["id"] in self._LastRelated:
                self._LastRelated.append(Item["id"])
                return Item

        self._LastRelated.clear()
        return Data[0]
