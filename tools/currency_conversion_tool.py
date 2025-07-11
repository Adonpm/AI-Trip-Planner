import os
from utils.currency_converter import CurrencyConverter
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class CurrencyConversionTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("EXCHANGE_RATE_API_KEY")
        self.currency_service = CurrencyConverter(self.api_key)
        self.currency_converter_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        '''Setup all tools for the currency converter tool'''
        @tool
        def convert_currency(amount:float, from_currency:str, to_currency:str) -> float:
            ''' Convert amount from one currency to another'''
            converted_amount = self.currency_service.convert(amount, from_currency, to_currency)
            return converted_amount
        
        return [convert_currency]
