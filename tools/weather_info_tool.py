import os
from typing import List
from dotenv import load_dotenv
from langchain.tools import tool
from utils.weather_info import WeatherInfo

class WeatherInfoTool:
    def __init__(self):
        load_dotenv()
        self.api_key=os.getenv("OPENWEATHERMAP_API_KEY")
        self.weather_info=WeatherInfo(self.api_key)
        self.weather_tool_list=self._setup_tools()

    def _setup_tools(self) -> List:
        '''Setup all tools for the weather current & forecast tool'''
        @tool
        def get_current_weather(place:str) -> str:
            '''Fetches current weather info of a place'''
            current_weather = self.weather_info.get_current_weather(place)
            if current_weather:
                temp = current_weather.get('main', {}).get('temp', "N/A")
                desc = current_weather.get('weather', [{}])[0].get('description', "N/A")
                return f"Current weather in {place} is {temp}°C, {desc}"
            return f"Couldnot fetch weather for {place}"
        
        @tool
        def get_forecast_weather(place:str) -> str:
            '''Fetches forecast weather of a place'''
            forecast_weather = self.weather_info.get_forecast_weather(place)
            if forecast_weather and 'list' in forecast_weather:
                forecast_summary = []
                for i in range(len(forecast_weather['list'])):
                    item = forecast_weather['list'][i]
                    date = item['dt_txt'].split(' ')[0]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description']
                    forecast_summary.append(f"{date}: {temp} degree celcius, {desc}")
                return f"Weather forecast for {place}:\n" + "\n".join(forecast_summary)
            return f"Couldnt fetch forecast for {place}"
        
        return [get_current_weather, get_forecast_weather]
