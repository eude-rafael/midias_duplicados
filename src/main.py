#from modules.test.necessary_resources import VerificadorDeArquivos
from src.modules.tela.interacao import MeuApp

class AppMain:
    def __init__(self):
        MA = MeuApp()
        MA.executar()
