import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from urllib.parse import quote
 
 
class MeuApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Minha Janela")
        self.root.geometry("950x500")  # Definindo a largura e altura da janela
        self.root.configure(bg="#444654")

    def action_segundo_botao(self, files):
        urln = self.folder_path.replace("/", "\\")        
        i=1

        for file in files:
            image_path = urln+'\\'+file
            self.imprimi_imagem(image_path)

    def imprimi_imagem(self, image_path):
        left = 10
        top = 100
        image = ""

        image = Image.open(image_path)

        # Redimensionando a imagem (opcional)
        image.thumbnail((200, 200))
        # Criando o objeto PhotoImage a partir da imagem
        photo = ImageTk.PhotoImage(image)

        # Exibindo a imagem na janela usando um Label
        image_label = tk.Label(self.root, image=photo)
        image_label.place(x=left, y=top)  # Posicionando o Label com a imagem em coordenadas específicas
        
        self.root.mainloop()

        image = ""
        photo = ""

        if(left< 1200):
            left = left + 350
        else:
            left = 10
            top = top + 350


    def verifica_lista_de_arquivos(self):
        self.folder_path = filedialog.askdirectory()
        file_label = tk.Label(self.root, text="Nenhum arquivo")
        file_label.pack() 

        if self.folder_path:
            files = os.listdir(self.folder_path)
            self.action_segundo_botao(files)
        else:
            file_label.config(text="Nenhuma pasta selecionada")

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            print("Pasta selecionada:", folder_path)



    def executar(self):
        button = tk.Button(self.root, text="Selecionar pasta das ocorrencias", command=self.select_folder, bg="#353740", fg="#ffffff")
        button.place(x=10, y=25)  # Posicionando o botão em coordenadas específicas

        button = tk.Button(self.root, text="Verificar ocorrencias", command=self.verifica_lista_de_arquivos, bg="#353740", fg="#ffffff")
        button.place(x=200, y=25)  # Posicionando o botão em coordenadas específicas

        self.root.mainloop()
 