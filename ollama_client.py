import requests


class OllamaClient:
    def __init__(self):
        self.url = "http://localhost:11434/api/chat"
        self.dados = {
                "model": "qwen3:4b",
                "stream": False,
                "messages":
                [
                    {
                    "role": "user",
                    "content": None
                    }
                ]
        }
    
    def chat(self, message:str) -> str:
        self.dados["messages"][0]["content"] = message
        resposta = requests.post(self.url, json=self.dados)
        dados_resposta = resposta.json()
        return dados_resposta["message"]["content"]
        

