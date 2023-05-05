import os
import tkinter as tk
from tkinter import filedialog


class TelaPastaRaiz:

    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Selecionando pasta")
        self.entrada = tk.Entry(self.janela)
        self.mensagem = tk.Label(self.janela)
        self.criar_tela()


    def verificar_pasta(self):
        caminho_pasta = self.entrada.get()
        if not os.path.isfile(caminho_pasta):
            self.mensagem["text"] = 'A pasta não existe.\nOu nenhuma pasta foi selecionada.'
        else:
            self.janela.quit()
            return caminho_pasta


    def selecionar_pasta(self):
        caminho_pasta = filedialog.askdirectory()
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, caminho_pasta)


    def criar_tela(self):
        # Criando widgets
        label = tk.Label(self.janela, text="Digite ou selecione o caminho da pasta:")
        botao_selecionar = tk.Button(self.janela, text="Selecionar pasta", command=self.selecionar_pasta)
        botao_confirmar = tk.Button(self.janela, text="Confirmar pasta", command=self.verificar_pasta)

        # Definindo o layout dos widgets
        label.grid(row=0, column=0, sticky="W")
        self.entrada.grid(row=1, column=0, padx=5, pady=5, sticky="WE")
        botao_selecionar.grid(row=1, column=1, padx=5, pady=5, sticky="W")
        botao_confirmar.grid(row=2, column=0, padx=5, pady=5, sticky="WE")
        self.mensagem.grid(row=3, column=0, padx=5, pady=5, sticky="W")

        # Configuração a janela ficar no topo e manter o foco.
        self.janela.attributes('-topmost', True)
        self.janela.focus_force()

        # Rodando a janela principal
        self.janela.mainloop()
