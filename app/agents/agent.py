import os
from dotenv import load_dotenv

from strands import Agent
from strands.models.ollama import OllamaModel

from app.tools.calculator import calculator


load_dotenv()


OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME")

if not OLLAMA_BASE_URL or not OLLAMA_MODEL_NAME:
    raise ValueError("As variáveis OLLAMA_BASE_URL e OLLAMA_MODEL_NAME devem estar definidas no .env")


ollama_model = OllamaModel(
    model_id=OLLAMA_MODEL_NAME,
    host=OLLAMA_BASE_URL
)


chat_agent = Agent(
    model=ollama_model,
    tools=[calculator]
)


__all__ = ["chat_agent"]