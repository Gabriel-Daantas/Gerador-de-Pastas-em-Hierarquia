import os
import tkinter as tk
from tkinter import filedialog


class TelaArquivo:

    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Selecionando arquivo")
        self.entrada = tk.Entry(self.janela)
        self.mensagem = tk.Label(self.janela)
        self.criar_tela()


    def verificar_arquivo(self):
        caminho_arquivo = self.entrada.get()
        if not os.path.isfile(caminho_arquivo):
            self.mensagem["text"] = 'O arquivo não existe.\nOu nenhum arquivo foi selecionado.'
        else:
            self.janela.quit()
            return caminho_arquivo


    def selecionar_arquivo(self):
        caminho_arquivo = filedialog.askopenfilename()
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, caminho_arquivo)


    def criar_tela(self):
        # Criando widgets
        label = tk.Label(self.janela, text="Digite ou selecione o caminho do arquivo:")
        botao_selecionar = tk.Button(self.janela, text="Selecionar arquivo", command=self.selecionar_arquivo)
        botao_confirmar = tk.Button(self.janela, text="Confirmar arquivo", command=self.verificar_arquivo)

        # Definindo o layout dos widgets
        label.grid(row=0, column=0, sticky="W")
        self.entrada.grid(row=1, column=0, padx=5, pady=5, sticky="WE")
        botao_selecionar.grid(row=1, column=1, padx=5, pady=5, sticky="W")
        botao_confirmar.grid(row=2, column=0, padx=5, pady=5, sticky="WE")
        self.mensagem.grid(row=3, column=0, padx=5, pady=5, sticky="W")

        # Configuração a janela ficar no topo e manter o foco.
        self.janela.attributes('-topmost', True)
        self.janela.focus_force()

        self.janela.mainloop()