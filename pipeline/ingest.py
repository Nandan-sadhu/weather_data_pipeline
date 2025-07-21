import requests
import logging

def fetch_weather_data(latitude=22.57, longitude=88.36):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info("API fetch successful")
        return response.json()
    except Exception as e:
        logging.error(f"Error in fetch_weather_data: {e}")
        return None