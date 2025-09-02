import requests, datetime
from dotenv import load_dotenv
import os

def sun_risen():
    """Returns boolean, True if sun has risen
    """
    #gets key from .env
    load_dotenv()
    api_key = os.getenv("WEATHER_KEY")

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    city_name = "Birmingham, GB"
    complete_url = base_url + "?appid=" + api_key + "&q=" + city_name
    #calls OpenWeather API 
    response = requests.get(complete_url)
    x = response.json()
    #if request was successful
    if x["cod"] != "404":
        y = x["sys"]
        sunrise_unix = datetime.datetime.fromtimestamp(y["sunrise"])
        current_time = datetime.datetime.now()
        #return true if sun has risen
        return (current_time >= sunrise_unix )
        