import requests
import pandas as pd
import time

BASE_URL = "https://backend.delhimetrorail.com/api/v2/en/station/"
LINE_STATION_API = "https://backend.delhimetrorail.com/api/v2/en/station_by_line_linepage/LN11"


def fetch_station_codes():
    response = requests.get(LINE_STATION_API)
    response.raise_for_status()
    data = response.json()

    return [s.get("station_code") for s in data if s.get("station_code")]


def fetch_station_data(station_code):
    url = BASE_URL + station_code
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def transform_station_data(data):
    previous_station = None
    next_station = None

    prev_next = data.get("prev_next_stations", [])

    try:
        if prev_next and "Rapid Metro" in prev_next[0]:
            line_data = prev_next[0]["Rapid Metro"][0]

            prev_raw = line_data.get("prev_station")
            next_raw = line_data.get("next_station")

            if isinstance(prev_raw, dict):
                previous_station = prev_raw.get("station_name")
            elif isinstance(prev_raw, str):
                previous_station = prev_raw

            if isinstance(next_raw, dict):
                next_station = next_raw.get("station_name")
            elif isinstance(next_raw, str):
                next_station = next_raw

    except Exception as e:
        print("Warning: prev/next parse failed:", e)

    lifts = data.get("lifts", [])
    has_lift = any(l["lift_type"] == "Lift" for l in lifts)
    has_escalator = any(l["lift_type"] == "Escalator" for l in lifts)

    parkings = data.get("parkings", [])
    parking_available = any(
        p.get("capacity_car", 0) > 0 or p.get("capacity_motorcycle", 0) > 0
        for p in parkings
    )

    metro_lines = data.get("metro_lines", [])
    line_color = metro_lines[0].get("line_color") if metro_lines else None

    return {
        "station_code": data.get("station_code"),
        "station_name": data.get("station_name"),
        "station_type": data.get("station_type"),
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "line_color": line_color,
        "landline": data.get("landline"),
        "previous_station": previous_station,
        "next_station": next_station,
        "has_lift": has_lift,
        "has_escalator": has_escalator,
        "is_interchange": data.get("interchange"),
        "parking_available": parking_available
    }


def main():
    rows = []

    station_codes = fetch_station_codes()
    print(f"Fetched {len(station_codes)} station codes dynamically")

    for code in station_codes:
        print(f"Processing station: {code}")
        raw_data = fetch_station_data(code)
        clean_row = transform_station_data(raw_data)
        rows.append(clean_row)
        time.sleep(0.5)

    df = pd.DataFrame(rows)
    df.to_csv("stations.csv", index=False)
    print("stations.csv created successfully")


if __name__ == "__main__":
    main()
