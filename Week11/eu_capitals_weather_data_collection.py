import requests
import json
import time
from datetime import datetime

#eu capital reference list already provided.
EU_CAPITALS = [
 {"city": "Vienna", "country": "Austria",
 "lat": 48.2082, "lon": 16.3738},
 {"city": "Brussels", "country": "Belgium",
 "lat": 50.8503, "lon": 4.3517},
 {"city": "Sofia", "country": "Bulgaria",
 "lat": 42.6977, "lon": 23.3219},
 {"city": "Zagreb", "country": "Croatia",
 "lat": 45.8150, "lon": 15.9819},
 {"city": "Nicosia", "country": "Cyprus",
 "lat": 35.1856, "lon": 33.3823},
 {"city": "Prague", "country": "Czechia",
 "lat": 50.0755, "lon": 14.4378},
 {"city": "Copenhagen", "country": "Denmark",
 "lat": 55.6761, "lon": 12.5683},
 {"city": "Tallinn", "country": "Estonia",
 "lat": 59.4370, "lon": 24.7536},
 {"city": "Helsinki", "country": "Finland",
 "lat": 60.1695, "lon": 24.9354},
 {"city": "Paris", "country": "France",
 "lat": 48.8566, "lon": 2.3522},
 {"city": "Berlin", "country": "Germany",
 "lat": 52.5200, "lon": 13.4050},
 {"city": "Athens", "country": "Greece",
 "lat": 37.9838, "lon": 23.7275},
 {"city": "Budapest", "country": "Hungary",
 "lat": 47.4979, "lon": 19.0402},
 {"city": "Dublin", "country": "Ireland",
 "lat": 53.3498, "lon": -6.2603},
 {"city": "Rome", "country": "Italy",
 "lat": 41.9028, "lon": 12.4964},
 {"city": "Riga", "country": "Latvia",
 "lat": 56.9496, "lon": 24.1052},
 {"city": "Vilnius", "country": "Lithuania",
 "lat": 54.6872, "lon": 25.2797},
 {"city": "Luxembourg", "country": "Luxembourg",
 "lat": 49.6116, "lon": 6.1319},
 {"city": "Valletta", "country": "Malta",
 "lat": 35.8989, "lon": 14.5146},
 {"city": "Amsterdam", "country": "Netherlands",
 "lat": 52.3676, "lon": 4.9041},
 {"city": "Warsaw", "country": "Poland",
 "lat": 52.2297, "lon": 21.0122},
 {"city": "Lisbon", "country": "Portugal",
 "lat": 38.7223, "lon": -9.1393},
 {"city": "Bucharest", "country": "Romania",
 "lat": 44.4268, "lon": 26.1025},
 {"city": "Bratislava", "country": "Slovakia",
 "lat": 48.1486, "lon": 17.1077},
 {"city": "Ljubljana", "country": "Slovenia",
 "lat": 46.0569, "lon": 14.5058},
 {"city": "Madrid", "country": "Spain",
 "lat": 40.4168, "lon": -3.7038},
 {"city": "Stockholm", "country": "Sweden",
 "lat": 59.3293, "lon": 18.0686}
]

#API INTEGRATION weather codes, current_weather hourly. temp, percip prob,
WEATHER_CODES = {
0: "Clear sky",
 1: "Mainly clear",
 2: "Partly cloudy",
 3: "Overcast",
 45: "Fog",
 48: "Depositing rime fog",
 51: "Drizzle (light)",
 53: "Drizzle (moderate)",
 55: "Drizzle (dense)",
 56: "Freezing Drizzle (light)",
 57: "Freezing Drizzle (dense)",
 61: "Rain (slight)",
 63: "Rain (moderate)",
 65: "Rain (heavy)",
 66: "Freezing Rain (light)",
 67: "Freezing Rain (heavy)",
 71: "Snow fall (slight)",
 73: "Snow fall (moderate)",
 75: "Snow fall (heavy)",
 77: "Snow grains",
 80: "Rain showers (slight)",
 81: "Rain showers (moderate)",
 82: "Rain showers (violent)",
 85: "Snow showers (slight)",
 86: "Snow showers (heavy)",
 95: "Thunderstorm",
 96: "Thunderstorm (slight hail)",
 97: "Thunderstorm (heavy hail)"
}

#weather data
def get_weather_data(lat, lon):
    url ="https://api.open-meteo.com/v1/forecast"
    today = datetime.today().strftime("%Y-%m-%d")
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "start_date": today,
        "end_date": today,
        "hourly": "temperature_2m,precipitation_probability,weathercode",
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error getting data for ({lat}, {lon}): {e}")
        return None

#Process data
def process_weather_data(raw_data, city, country):
    try:
        current = raw_data.get("current_weather", {})
        hourly = raw_data.get("hourly", {})
        forecast_list = []

        if all(k in hourly for k in ("time", "temperature_2m", "precipitation_probability", "weathercode")):
            for i in range(len(hourly["time"])):
                forecast_list.append({
                    "time": hourly["time"][i],
                    "temperature": hourly["temperature_2m"][i],
                    "precipitation_probability": hourly["precipitation_probability"][i],
                    "weathercode": hourly["weathercode"][i],
                    "condition": WEATHER_CODES.get(hourly["weathercode"][i], "Unknown")
                })
        return {
            "city": city,
            "country": country,
            "coordinates": {"latitude": raw_data.get("latitude"), "longitude": raw_data.get("longitude")},
            "current_weather": {
                "temperature": current.get("temperature"),
                "windspeed": current.get("windspeed"),
                "weathercode": current.get("weathercode"),
                "condition": WEATHER_CODES.get(current.get("weathercode"), "Unknown"),
                "time": current.get("time")
            },
            "hourly_forecast": forecast_list
        }
    except Exception as e:
        print(f"Error processing {city}: {e}")
        return None

# collect weather data use delay 0.5-1 second
def collect_eu_weather_data(delay =0.8):
    weather_data = {}

    print("Collecting EU Capital Weather Data...\n")

    for i, cap in enumerate(EU_CAPITALS):
        city = cap["city"]
        country = cap["country"]

        print(f"> Getting: {city} ({i + 1}/{len(EU_CAPITALS)})")
        raw = get_weather_data(cap["lat"], cap["lon"])
        if raw:
            processed = process_weather_data(raw, cap["city"], cap["country"])

            if processed:
                weather_data[cap["city"]] = processed
                print(f" Success! {cap['city']}")

            else:
                print(f" Processing failed for {cap['city']}")
        else:
            print(f" Request failed for {cap['city']}")
            time.sleep(delay)
    return weather_data


#SAVE TO JSON
def save_json(data, filename="eu_weather_data.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\nSaved {len(data)} cities to {filename}")

    except IOError as e:
        print(f"Error saving JSON: {e}")


# MAIN FUNCTION
def main():
    print("#############################################")
    print("# EUROPEAN CAPITAL WEATHER REPORT TOOL #")
    print("#############################################\n")

    weather_data = collect_eu_weather_data()
    save_json(weather_data)
    print("\nData Collection is Complete!")

if __name__ == "__main__":
    main()




