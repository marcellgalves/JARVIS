import requests
import logging

logger = logging.getLogger(__name__)

class OllamaClient:
    def __init__(self):
        self.url = "http://localhost:11434/api/chat"
        self.dados = {
                "model": "qwen3:4b",
                "stream": False,
                "messages":[]
        }

    
    def chat(self, message:str) -> str:
        nova_mensagem = {
            "role": "user",
            "content": message
        }
        self.dados["messages"].append(nova_mensagem)
        try:
            resposta = requests.post(self.url, json=self.dados, timeout=60)
            resposta.raise_for_status()
            dados_resposta = resposta.json()
            self.dados["messages"].append(dados_resposta["message"])
            
            return dados_resposta["message"]["content"]
        except requests.exceptions.ConnectionError:
            logger.error("Não foi possível conectar ao Ollama.")
            return "JARVIS: Não foi possível conectar ao Ollama."
        except requests.exceptions.Timeout:
            logger.error("Ollama server demorou demais para responder.")
            return "Ollama server demorou demais para responder."
        except requests.exceptions.HTTPError:
            logger.error("Erro HTTP na comunicação com o Ollama.")
            return "Erro HTTP na comunicação com o Ollama."