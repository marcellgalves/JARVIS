from ollama_client import OllamaClient
import logging
logger = logging.getLogger(__name__)


class JarvisCore:
    def __init__(self):
        self.client = OllamaClient()
        self.nome = "JARVIS"
        self.commands_dict = {
            '/help': self.help,
            '/version': self.version,
            '/apresentar': self.apresentar,
            '/somar': self.somar,
            '/repetir': self.repetir,
            '/memoria': self.memoria,
        }
    
    def process_message(self, message: str) -> str:
        elementos_mensagem = message.split()   
        if not elementos_mensagem:
            return ""
        command = elementos_mensagem[0]
        if command in self.commands_dict:
            resto_command = elementos_mensagem[1:]
            logger.info(f"Comando {command} recebido.")
            return self.commands_dict[command](resto_command)
        elif command.startswith("/"):
            return "JARVIS: Comando não reconhecido."
        return self.client.chat(message) 
        









    def help(self, args: list[str]) -> str:
        return "\n /help -> exibe todos os comandos de JARVIS disponiveis. " \
        " \n /version -> exibe a versao do programa. " \
        "\n /apresentar -> apresenta JARVIS ao usuário. " \
        "\n /somar (int a, int b) -> soma dois números e devolve o resultado. " \
        "\n /repetir (str mensagem) -> repete a mensagem digitada pelo usuário. " \
        "\n /exit -> Encerra JARVIS. " \
        "\n /memoria -> exibe a memória do chat de User - JARVIS"
    def version(self, args: list[str]) -> str:
        return "JARVIS 0.1.1"
    def apresentar(self, args: list[str]) -> str:
        return f"Olá, meu nome é {self.nome}, o seu assistente pessoal!"
    def somar(self, args: list[str]) -> str:
        if len(args) != 2:
            logger.error("Quantidade incorreta de parametros na função /somar.")
            return "Erro: Quantidade incorreta de parametros. "
        try:
            resultado = int(args[0]) + int(args[1])
            return f'Resultado: {resultado}'
        except ValueError:
            logger.error("Formato de parametro(s) incorreto")
            return "Erro: digite parametros corretos. "
    def repetir(self, args: list[str]) -> str:
        frase = " ".join(args)
        return f"JARVIS: {frase}"
    def memoria(self, args: list[str]):
        historico = self.client.dados["messages"]
        linhas = []
        for mensagem in historico:
            linhas.append(f'{mensagem["role"]}: {mensagem["content"]}')
        return "\n ".join(linhas)





