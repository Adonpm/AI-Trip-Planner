import os
from utils.place_info_search import GooglePlaceSearch, TavilyPlaceSearch
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_places_api_key = os.getenv("GPLACES_API_KEY")
        self.google_places_search = GooglePlaceSearch(self.google_places_api_key)
        os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
        self.tavily_search = TavilyPlaceSearch()
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        '''Setup all tools for the place search tool'''
        @tool
        def search_attractions(place:str) -> str:
            '''Search top attractions of a place'''
            try:
                google_attraction_result = self.google_places_search.google_search_attractions(place)
                if google_attraction_result:
                    return f"Following are the attractions of {place} as suggested by google: {google_attraction_result}"
            except Exception as e:
                tavily_attraction_result = self.tavily_search.tavily_search_attractions(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the attractions of {place}: {tavily_attraction_result}" ## Fallback search using tavily in case google places fail
            
        @tool
        def search_restaurants(place:str) -> str:
            '''Search restaurants of a place'''
            try:
                google_restaurants_result = self.google_places_search.google_search_restaurants(place)
                if google_restaurants_result:
                    return f"Following are the restaurants of {place} as suggested by google: {google_restaurants_result}"
            except Exception as e:
                tavily_restaurants_result = self.tavily_search.tavily_search_restaurants(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the restaurants of {place}: {tavily_restaurants_result}" ## Fallback search using tavily in case google places fail

        @tool
        def search_activities(place:str) -> str:
            '''Search top activities of a place'''
            try:
                google_activities_result = self.google_places_search.google_search_activity(place)
                if google_activities_result:
                    return f"Following are the attractions of {place} as suggested by google: {google_activities_result}"
            except Exception as e:
                tavily_activities_result = self.tavily_search.tavily_search_activity(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the activities of {place}: {tavily_activities_result}" ## Fallback search using tavily in case google places fail
            
        @tool
        def search_transportation(place:str) -> str:
            '''Search different transportation modes of a place'''
            try:
                google_transportation_result = self.google_places_search.google_search_transportation(place)
                if google_transportation_result:
                    return f"Following are the attractions of {place} as suggested by google: {google_transportation_result}"
            except Exception as e:
                tavily_transportation_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the transportation modes of {place}: {tavily_transportation_result}" ## Fallback search using tavily in case google places fail
            
        return [search_attractions, search_restaurants, search_activities, search_transportation]
            