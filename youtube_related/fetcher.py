import aiohttp
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}


def fetch(vURL: str) -> str:
    with requests.get(vURL, headers=headers) as response:
        RAW = response.text
    return RAW


async def async_fetch(vURL: str) -> str:
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(vURL) as response:
            RAW = await response.text()
    return RAW
