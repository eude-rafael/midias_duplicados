import os
import time

class VerificadorDeArquivos:
    def __init__(self, pasta, intervalo_verificacao, acao):
        self.pasta = pasta
        self.intervalo_verificacao = intervalo_verificacao
        self.acao = acao
        self.arquivos_anteriores = []

    def iniciar_verificacao(self):
        while True:
            arquivos_atuais = self.obter_arquivos()
            arquivos_novos = self.obter_arquivos_novos(arquivos_atuais)

            if arquivos_novos:
                self.acao(arquivos_novos)

            self.arquivos_anteriores = arquivos_atuais
            time.sleep(self.intervalo_verificacao)

    def obter_arquivos(self):
        return os.listdir(self.pasta)

    def obter_arquivos_novos(self, arquivos_atuais):
        return [arquivo for arquivo in arquivos_atuais if arquivo not in self.arquivos_anteriores]


