import requests
import pandas as pd
import time
from datetime import datetime
from itertools import permutations

ROUTE_BASE_URL = "https://backend.delhimetrorail.com/api/v2/en/station_route"
LINE_STATION_API = "https://backend.delhimetrorail.com/api/v2/en/station_by_line_linepage/LN11"


def fetch_station_codes():
    response = requests.get(LINE_STATION_API)
    response.raise_for_status()
    data = response.json()
    return [s.get("station_code") for s in data if s.get("station_code")]


def fetch_route_data(from_station, to_station):
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]

    url = f"{ROUTE_BASE_URL}/{from_station}/{to_station}/least-distance/{timestamp}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Referer": "https://www.delhimetrorail.com/",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def transform_route_data(data, from_code, to_code):
    routes = data.get("route", [])
    route = routes[0] if routes else {}

    return {
        "from_code": from_code,
        "to_code": to_code,
        "from_name": data.get("from"),
        "to_name": data.get("to"),
        "fare": data.get("fare"),
        "total_travel_time": data.get("total_time"),
        "total_stations": data.get("stations"),
        "line": route.get("line"),
        "towards_station": route.get("towards_station"),
        "platform": route.get("platform_name"),
        "first_train_time": route.get("new_start_time"),
        "last_train_time": route.get("new_end_time"),
    }


def main():
    rows = []

    station_codes = fetch_station_codes()
    station_pairs = list(permutations(station_codes, 2))

    print(f"Processing {len(station_pairs)} route combinations")

    for from_st, to_st in station_pairs:
        try:
            print(f"Fetching route: {from_st} → {to_st}", end="\r")
            raw = fetch_route_data(from_st, to_st)
            clean = transform_route_data(raw, from_st, to_st)
            rows.append(clean)
            time.sleep(0.5)

        except Exception as e:
            print(f"\nFailed for {from_st} → {to_st}: {e}")

    df = pd.DataFrame(rows)
    df.to_csv("metro_routes_data.csv", index=False)
    print("\nmetro_routes_data.csv created successfully")


if __name__ == "__main__":
    main()
