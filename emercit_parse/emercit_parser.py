from typing import List, Dict

import requests
from fake_useragent import UserAgent

from dataclasses import dataclass

ua = UserAgent()

town_to_detector: Dict[str, str] = {
    "Горячий Ключ": "АГК-0088",
    "Пятигорская": "ЭМЕРСИТ-0007Д",
}
towns: List[str] = list(town_to_detector.keys())


@dataclass(slots=True, frozen=True)
class RiverData:
    current_river_level: float
    prevention_level: float
    danger_level: float
    time: str


def get_river_data(town: str):
    data = get_data("http://emercit.com/map/overall.php")
    town_data = get_town_data(data, town)
    parsed_data = parse_town_data(town_data)
    return parsed_data


def parse_town_data(town_data) -> RiverData:
    river_level = town_data["data"]["river_level"]
    return RiverData(
        current_river_level=round(river_level["level"]["bs"], 3),
        prevention_level=river_level["prevention"]["bs"],
        danger_level=river_level["danger"]["bs"],
        time=river_level["time"],
    )


def get_town_data(data: dict, town: str) -> dict[str, float] | None:
    features = data["features"]
    for feature in features:
        if feature["properties"]["name"] == town_to_detector[town]:
            town_data = feature["properties"]

            return town_data


def get_data(url: str) -> dict[str, float | None]:
    headers = {
        "Accept": "*/*",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "http://emercit.com/map/",
        "User-Agent": ua.random,
        "X-Requested-With": "XMLHttpRequest",
    }

    response = requests.get(url, headers=headers, verify=False).json()

    return response


if __name__ == "__main__":
    print(get_river_data("Пятигорская"))
