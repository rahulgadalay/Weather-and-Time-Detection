import datetime
from zoneinfo import ZoneInfo

import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

from google.adk.agents import Agent


def get_weather(city: str) -> dict:
    """
    Retrieves live weather for any city using Open-Meteo.
    """

    try:
        geolocator = Nominatim(user_agent="weather_agent")
        location = geolocator.geocode(city)

        if location is None:
            return {
                "status": "error",
                "error_message": f"Could not find city '{city}'."
            }

        latitude = location.latitude
        longitude = location.longitude

        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            f"&current_weather=true"
        )

        response = requests.get(
            url,
            timeout=10
        )
        if response.status_code != 200:
            return {
                "status": "error",
                "error_message": "Unable to fetch weather information."
            }

        data = response.json()

        weather = data["current_weather"]

        return {
            "status": "success",
            "report": (
                f"Current weather in {city}:\n"
                f"Temperature : {weather['temperature']}°C\n"
                f"Wind Speed  : {weather['windspeed']} km/h\n"
                f"Weather Code: {weather['weathercode']}"
            )
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": str(e)
        }


def get_current_time(city: str) -> dict:
    """
    Returns the current local time for any city.
    """

    try:
        geolocator = Nominatim(user_agent="time_agent")
        location = geolocator.geocode(city)

        if location is None:
            return {
                "status": "error",
                "error_message": f"Could not find city '{city}'."
            }

        tf = TimezoneFinder()

        timezone = tf.timezone_at(
            lat=location.latitude,
            lng=location.longitude
        )

        if timezone is None:
            return {
                "status": "error",
                "error_message": f"Timezone not found for {city}."
            }

        now = datetime.datetime.now(
            ZoneInfo(timezone)
        )

        return {
            "status": "success",
            "report": (
                f"The current time in {city} is "
                f"{now.strftime('%Y-%m-%d %I:%M:%S %p')}"
            )
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": str(e)
        }


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-3.1-flash-lite",
    description=(
        "AI Agent that provides live weather and current time for any city."
    ),
    instruction=(
        "You are a helpful AI assistant. "
        "Whenever a user asks about weather or time, "
        "use the available tools and answer naturally."
    ),
    tools=[
        get_weather,
        get_current_time,
    ],
)