import os
from dotenv import load_dotenv

from fastapi import FastAPI
from pydantic import BaseModel

from strands import Agent
from strands import tool
from strands.models.ollama import OllamaModel


# from strands_agents.agents import Agent
# from strandsagents.llms import OllamaLLM
# from strands_agents.tools import Tool, tool


load_dotenv()


OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME")

if not OLLAMA_BASE_URL or not OLLAMA_MODEL_NAME:
    raise ValueError("As variáveis OLLAMA_BASE_URL e OLLAMA_MODEL_NAME devem estar configuradas no .env")




app = FastAPI(
    title="API de Chat com Agente Ollama",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str



@tool
def calculator(operation: str) -> str:
    """
    Use esta ferramenta para resolver operações matemáticas e expressões.
    A entrada deve ser a operação matemática (ex: '1234 * 5678' ou 'sqrt(144)').
    """
    try:

        import math
        operation = operation.replace("sqrt","math.sqrt")

        result = eval(operation)
        return str(result)
    except Exception as e:
        return f"Erro ao calcular: {e}"
    


ollama_model = OllamaModel(
    model_id=OLLAMA_MODEL_NAME,
    host=OLLAMA_BASE_URL
)

chat_agent = Agent(model=ollama_model, tools=[calculator])



# @app.post("/chat", response_model=ChatResponse)
# async def chat_endpoint(request: ChatRequest):
#     """
#     Recebe uma mensagem do usuário, envia para o Agente de IA e retorna a resposta.
#     """

#     user_message = request.message

#     response = await chat_agent.chat(user_message)

#     return ChatResponse(response=response)

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    agent_response = await chat_agent(request.message)
    return ChatResponse(response=agent_response.message)