from strands import tool
import math
import re

@tool
def calculator(operation: str) -> str:
    """
    Use esta ferramenta para resolver operações matemáticas e expressões.
    A entrada deve ser a operação matemática (ex: '1234 * 5678' ou 'sqrt(144)').
    """
    try:

    
        operation = operation.replace("sqrt","math.sqrt")

        result = eval(operation)
        return str(result)
    except Exception as e:
        return f"Erro ao calcular: {e}"
    
