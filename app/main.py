import os
import json
from dotenv import load_dotenv

from fastapi import FastAPI
from pydantic import BaseModel

from strands import Agent
from strands import tool
from strands.models.ollama import OllamaModel

from app.tools.calculator import calculator
from app.agents.agent import chat_agent






app = FastAPI(
    title="API de Chat com Agente Ollama",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str



@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        agent_response = chat_agent(request.message)
        
        # Extrai o texto da resposta
        content_list = agent_response.message.get('content', [])
        if content_list and 'text' in content_list[0]:
            response_text = content_list[0]['text']
        else:
            response_text = str(agent_response)
        
        # Verifica se é uma chamada para a calculadora
        if response_text.strip().startswith('{'):
            try:
                tool_call = json.loads(response_text)
                if (tool_call.get('name') == 'calculator' and 
                    'operation' in tool_call.get('arguments', {})):
                    
                    operation = tool_call['arguments']['operation']
                    result = calculator(operation)
                    return ChatResponse(response=result)
            except json.JSONDecodeError:
                pass  # Não é JSON válido, retorna o texto original
        
        return ChatResponse(response=response_text)
    
    except Exception as e:
        return ChatResponse(response=f"Erro: {str(e)}")