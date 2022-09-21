from pathlib import Path
from typing import Any

import requests

from d_api.constants import OPEN_WEATHER_API_KEY, TEMP_FOLDER_PATH, WEATHER_FILE_NAME


def _generate_uri(location: str) -> str:
    return f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={OPEN_WEATHER_API_KEY}&units=metric"


def get_forecast_to(location: str):
    weather_uri = _generate_uri(location)
    if (res := requests.get(weather_uri)) and res.status_code == 200:
        return res.json()


def extract_weather_data_from(location: str, forecast_data: dict[str, Any]) -> str:
    if weather_data := forecast_data.get("list"):
        return "\n".join(
            [
                f"{location}\t{item.get('dt_txt')}\t{item.get('main', {}).get('temp')}\t"
                + f"{item.get('weather', [{}])[-1].get('description')}"
                for item in weather_data
            ]
        )


def handle_file_content(location: str, file_content: str) -> None:
    with open(
        Path.joinpath(TEMP_FOLDER_PATH, f"{location}_{WEATHER_FILE_NAME}"), "a"
    ) as f:
        f.write("CITY\tTIME\tTEMPERATURE\tCONDITION\n")
        f.write(file_content)


def main(location: str) -> None:
    forecast_data = get_forecast_to(location)
    weather_data = extract_weather_data_from(location, forecast_data)
    handle_file_content(location, weather_data)


if __name__ == "__main__":
    location = "Stockholm"
    main(location)
