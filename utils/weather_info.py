import requests

class WeatherForecastTool:
    def __init__(self, api_key:str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def get_current_weather(self, place:str):
        '''Fetches current weather info of a place'''
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q" : place,
                "appid" : self.api_key
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise e
        
    def get_forecast_weather(self, place:str):
        '''Fetches forecast weather of a place'''
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q":place,
                "appid":self.api_key,
                "cnt": 10, # Get weather info for next 10 slots (30 hours)
                "units": "metric" # Weather is celsius
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise e
