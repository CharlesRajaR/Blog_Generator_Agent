from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

class GeminiLLM:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        try:
            os.environ["GOOGLE_API_KEY"] = self.gemini_api_key =  os.getenv("GOOGLE_API_KEY")
            llm = ChatGoogleGenerativeAI(model="gemini-3.7-flash")
            return llm
        except Exception as e:
            print(f"Unable to load llm : {e}")
