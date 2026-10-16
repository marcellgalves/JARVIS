class JarvisCore:
    def __init__(self):
        self.nome = "JARVIS"
        self.commands_dict = {
            '/help': self.help,
            '/version': self.version,
            '/apresentar': self.apresentar,
            '/somar': self.somar
        }
    
    def process_message(self, message: str) -> str:
        elementos_mensagem = message.split()   
        if not elementos_mensagem:
            return ""
        command = elementos_mensagem[0]
        if command in self.commands_dict:
            if command == "/somar":
                
                if len(elementos_mensagem) != 3:
                    return "Erro: quantidade incorreta de argumentos"
                try:
                    return f'Resultado: {self.somar(int(elementos_mensagem[1]),int(elementos_mensagem[2]))}'
                except ValueError:
                    return "Erro, digite os parametros corretos. "
            else:
                return self.commands_dict[command]()
            
        else:
            return f"JARVIS: Recebi sua mensagem: {message}" 
        









    def help(self) -> str:
        return "\n /help -> exibe todos os comandos de JARVIS disponiveis. " \
        " \n /version -> exibe a versao do programa. " \
        "\n /apresentar -> apresenta JARVIS ao usuário. " \
        "\n /somar (int a, int b) -> soma dois números e devolve o resultado. " \
        "\n /exit -> Encerra JARVIS. "
    def version(self) -> str:
        return "JARVIS 0.1.1"
    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}, o seu assistente pessoal!"
    def somar(self, a: int, b: int) -> int:
        return a + b
  




   





