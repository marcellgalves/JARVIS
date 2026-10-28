import requests
import logging

logger = logging.getLogger(__name__)

class OllamaClient:
    
    def __init__(self):
        self.url = "http://localhost:11434/api/chat"
        self.ferramenta_somar = {
                        "type": "function",
                        "function": {
                        "name": "somar",
                        "description": "Soma dois números inteiros.",
                        "parameters": {
                        "type": "object",
                        "properties": {
                        "a": {"type": "integer"},
                        "b": {"type": "integer"}
                        },
                        "required": ["a", "b"]
                        }
                        
                        },
                        
                    }
        self.dados = {
                "model": "qwen3:4b",
                "stream": False,
                "messages":[],
                "tools":[]
        }

        
        self.dados["tools"].append(self.ferramenta_somar)

    
    def chat(self, message:str) -> dict:
        nova_mensagem = {
            "role": "user",
            "content": message
        }
        self.dados["messages"].append(nova_mensagem)
        try:
            resposta = requests.post(self.url, json=self.dados, timeout=60)
            resposta.raise_for_status()

            dados_resposta = resposta.json()


            mensagem_ia = dados_resposta["message"]
            if mensagem_ia.get("tool_calls"):
                nome_ferramenta = mensagem_ia["tool_calls"][0]["function"]["name"]
                argumentos = mensagem_ia["tool_calls"][0]["function"]["arguments"]

                return {
                    "tipo": "ferramenta",
                    "nome": nome_ferramenta,
                    "argumentos": argumentos
                }
            else:
                self.dados["messages"].append(mensagem_ia)
                return {
                    "tipo": "texto",
                    "conteudo": mensagem_ia["content"]
                }
        except requests.exceptions.ConnectionError:
            logger.error("Não foi possível conectar ao Ollama.")
            return {
                   "tipo": "texto",
                   "conteudo": "Não foi possível conectar ao Ollama."
                    }
        except requests.exceptions.Timeout:
            logger.error("Ollama server demorou demais para responder.")
            return {
                   "tipo": "texto",
                   "conteudo": "Ollama server demorou demais para responder."
                    }
        except requests.exceptions.HTTPError:
            logger.error("Erro HTTP na comunicação com o Ollama.")
            return {
                   "tipo": "texto",
                   "conteudo": "Erro HTTP na comunicação com o Ollama."
                    }

