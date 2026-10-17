import requests

url = "http://localhost:11434/api/chat"

dados = {
    "model": "qwen3:4b",
    "messages": [
        {
            "role": "user",
            "content": "Olá! Quem é você?"
        }
    ],
    "stream": False
}

resposta = requests.post(url, json=dados)
dados_resposta = resposta.json()
print(dados_resposta["message"][0]["content"])