from collections import deque

from .fetcher import async_fetch, fetch
from .parser import parse


def get(vURL: str) -> list:
    RAW = fetch(vURL)
    Data = parse(RAW)

    return Data


async def async_get(vURL: str) -> list:
    RAW = await async_fetch(vURL)
    Data = parse(RAW)

    return Data


class preventDuplication:
    def __init__(self):
        self._LastRelated = deque(maxlen=10)

    def get(self, vURL: str) -> dict:
        Data = get(vURL)

        for Item in Data:
            if not Item["id"] in self._LastRelated:
                self._LastRelated.append(Item["id"])
                return Item

        self._LastRelated.clear()
        return Data[0]

    async def async_get(self, vURL: str) -> dict:
        Data = await async_get(vURL)

        for Item in Data:
            if not Item["id"] in self._LastRelated:
                self._LastRelated.append(Item["id"])
                return Item

        self._LastRelated.clear()
        return Data[0]
