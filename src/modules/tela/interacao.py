import tkinter as tk

class MeuApp:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Meu App")

        self.criar_elementos()

    def criar_elementos(self):
        self.rotulo = tk.Label(self.janela, text="Olá, mundo!")
        self.rotulo.pack()

        self.botao = tk.Button(self.janela, text="Clique Aqui", command=self.botao_clicado)
        self.botao.pack()

    def botao_clicado(self):
        print("Botão clicado!")

    def executar(self):
        self.janela.mainloop()

# Criando uma instância da classe MeuApp e executando o aplicativo
# app = MeuApp()
# app.executar()
