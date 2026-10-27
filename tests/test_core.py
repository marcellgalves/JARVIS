from core import JarvisCore
jarvis = JarvisCore()

def test_ia_soma_valida():
    assert jarvis.executar_ferramenta("somar", {"a": 10, "b": 20}) == "Resultado: 30"
def test_ia_ferramenta_inexistente():
    assert jarvis.executar_ferramenta("apagar_sistema", {}) == "Função inexistente/indisponível para JARVIS."
def test_ia_arg_invalido():
    assert jarvis.executar_ferramenta("somar", {"a": "abc", "b": 20}) == "Erro: digite parametros corretos. "
def test_ia_argumento_ausente():
    assert jarvis.executar_ferramenta(
        "somar", {"a": 10}
    ) == "Erro: argumento obrigatório ausente."



def test_help():
    assert jarvis.process_message("/help") == \
        "\n /help -> exibe todos os comandos de JARVIS disponiveis. " \
        "   \n /version -> exibe a versao do programa. " \
        "\n /apresentar -> apresenta JARVIS ao usuário. " \
        "\n /somar (int a, int b) -> soma dois números e devolve o resultado. " \
        "\n /repetir (str mensagem) -> repete a mensagem digitada pelo usuário. " \
        "\n /exit -> Encerra JARVIS. " \
        "\n /memoria -> exibe a memória do chat de User - JARVIS"

def test_version():
    assert jarvis.process_message("/version") == "JARVIS 0.1.2"
def test_somar():
    assert jarvis.process_message("/somar 20 10") == "Resultado: 30"
    assert jarvis.process_message("/somar -10 5") == "Resultado: -5"
def test_somar_argumentos_invalidos():
    assert jarvis.process_message("/somar abc 20") == "Erro: digite parametros corretos. "
def test_somar_quantidade_arg_invalidos():
    assert jarvis.process_message("/somar 10 20 30") == "Erro: Quantidade incorreta de parametros. "
    assert jarvis.process_message("/somar 10") == "Erro: Quantidade incorreta de parametros. "
def test_repetir():
    assert jarvis.process_message("/repetir Olá mundo") == "JARVIS: Olá mundo"
def test_apresentar():
    assert jarvis.process_message("/apresentar") == "Olá, meu nome é JARVIS, o seu assistente pessoal!"
def test_blank_message():
    assert jarvis.process_message("") == ""
