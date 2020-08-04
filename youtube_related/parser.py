import json
import re

DATA_JSON = re.compile(r'window\["ytInitialData"\]\s\=\s(\{.*\})')


def __loadInitialData(RAW: str) -> dict:
    Search = DATA_JSON.search(RAW)

    if not Search:
        raise ValueError

    RAW_DATA = Search.group(1)
    Data = json.loads(RAW_DATA)

    return Data


def parse(RAW: str) -> list:
    Data = __loadInitialData(RAW)

    Overlay = Data["playerOverlays"]["playerOverlayRenderer"]
    watchNextEndScreenRenderer = Overlay["endScreen"]["watchNextEndScreenRenderer"]
    Result = [
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
