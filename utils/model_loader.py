import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
load_dotenv()

class ConfigLoader:
    def __init__(self):
        print("Loading config....")
        self.config = load_config()
    def __getitem__(self, key):
        return self.config[key]

class ModelLoader(BaseModel):
    model_provider: Literal["groq", "openai"] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, __context:Any) -> None:
        self.config = ConfigLoader()
    
    class Config:
        arbitrary_types_allowed = True  # Allow using custom (non-Pydantic) classes like ConfigLoader

    def load_llm(self):
        '''
        Load and return llm model
        '''
        print("LLM Loading...")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Loading LLM from Groq..............")
            os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model = model_name)
            print("Groq LLM Loaded successfully")
        elif self.model_provider == "openai":
            print("Loading LLM from OpenAI..............")
            os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm = ChatOpenAI(model = model_name)
            print("OpenAI LLM Loaded successfully")
        return llm
