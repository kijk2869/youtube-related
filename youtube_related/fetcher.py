import aiohttp
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
}


def fetch(vURL: str) -> str:
    with requests.get(vURL, headers=headers) as response:
        RAW = response.text
    return RAW


async def async_fetch(vURL: str, local_addr: str = None) -> str:
    connector = aiohttp.TCPConnector(local_addr=(local_addr, 0)) if local_addr else None
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        async with session.get(vURL) as response:
            RAW = await response.text()
    return RAW
