import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesAPIWrapper, GooglePlacesTool
from dotenv import load_dotenv
load_dotenv()

class GooglePlaceSearch:
    def __init__(self, api_key:str):
        self.google_places_api_wrapper = GooglePlacesAPIWrapper(gplaces_api_key = api_key)
        self.google_places_tool = GooglePlacesTool(api_wrapper = self.google_places_api_wrapper)

    def google_search_attractions(self, place:str) -> dict:
        '''Searches for top attractions in the specified place using GooglePlaces API'''
        return self.google_places_tool.run(f"Top attractive places in and around {place}")

    def google_search_restaurants(self, place:str) -> dict:
        '''Searches for available restaurants in the specified place using GooglePlaces API'''
        return self.google_places_tool.run(f"What are the top 10 restaurants and eateries in and around {place}")

    def google_search_activity(self, place:str) -> dict:
        '''Searches for popular activities in the specified place using GooglePlaces API'''
        return self.google_places_tool.run(f"What are the popular activities in and around {place}")

    def google_search_transportation(self, place:str) -> dict:
        '''Searches for available transportation modes in the specified place using GooglePlaces API'''
        return self.google_places_tool.run(f"What are the available transportation modes in and around {place}")
    
class TavilyPlaceSearch:
    def __init__(self):
        os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
        self.tavily_tool = TavilySearch(topic="general", include_answer="advanced")

    def tavily_search_attractions(self, place:str):
        '''Searches for top attractions in the specified place using TavilySearch'''
        result = self.tavily_tool.invoke({"query": f"Top attractive places in and around {place}"})
        if isinstance (result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place:str):
        '''Searches for available restaurants in the specified place using TavilySearch'''
        result = self.tavily_tool.invoke({"query": f"What are the top 10 restaurants and eateries in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place:str):
        '''Searches for popular activities in the specified place using TavilySearch'''
        result = self.tavily_tool.invoke({"query": f"What are the popular activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_transportation(self, place:str):
        '''Searches for available transportation modes in the specified place using TavilySearch'''
        result = self.tavily_tool.invoke({"query": f"What are the available transportation modes in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    