import os
from dotenv import load_dotenv

load_dotenv()

class LLMConfig:
    def __init__(self):
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.groq_api_key = os.getenv("GROQ_API_KEY")
    
    def get_gemini_config(self, model="gemini-2.0-flash-exp"):
        return {
            "model": model,
            "api_key": self.gemini_api_key,
            "temperature": 0.7
        }
    
    def get_groq_config(self):
        return {
            "model": "grok-beta",
            "api_key": self.groq_api_key,
            "temperature": 0.7
        }
