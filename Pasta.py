import os

clear = lambda: os.system('cls')

class Pasta:
    def __init__(self, nome):
        self.nome = nome
        self.filhos = []


    def adicionar_filho(self, filho):
        self.filhos.append(filho)


    def criar_pasta(self, caminho):
        caminho_pasta = os.path.join(caminho, self.nome)
        if not os.path.exists(caminho_pasta):
            os.mkdir(caminho_pasta)
        for filho in self.filhos:
            filho.criar_pasta(caminho_pasta)


    def pastas_e_niveis(self, linhas):
        niveis = []
        pastas_e_niveis = {}
        dict_auxiliar = {}

        for linha in linhas:
            nivel_atual = int(linha.count('  ')/2)
            nome_pasta = linha.strip()

            if nivel_atual not in niveis:
                niveis.append(nivel_atual)
                pastas_e_niveis.update({nivel_atual: []})
                dict_auxiliar.update({nivel_atual: []})
    
            pastas_e_niveis[nivel_atual].append(linha.strip())

        return pastas_e_niveis, dict_auxiliar


    def criar_hierarquia_pastas(self, caminho_arquivo, raiz):
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        pasta_atual = raiz
        nivel_e_pastas, dict_auxiliar = self.pastas_e_niveis(linhas)
        pastas_pai = []

        for linha in linhas:
            nivel_atual = int(linha.count('  ')/2)
            nome_pasta = linha.strip()

            nova_pasta = Pasta(nome_pasta)

            if nivel_atual == 0:
                pasta_atual = raiz
            else:
                if nivel_atual == nivel_anterior:
                    pasta_atual = pasta_atual
                elif nivel_atual > nivel_anterior:
                    pasta_atual = pasta_atual.filhos[-1]
                else:
                    for nvl, pasta in nivel_e_pastas.items():
                        if nome_pasta in pasta:
                            for pai in pastas_pai:
                                if pai.nome == dict_auxiliar[nvl-1][-1]:
                                    pasta_atual = pai

            dict_auxiliar[nivel_atual].append(linha.strip())
            del nivel_e_pastas[nivel_atual][0]
            nivel_anterior = nivel_atual
            pastas_pai.append(pasta_atual)
            
            pasta_atual.adicionar_filho(nova_pasta)

        raiz.criar_pasta('.')


    def inicio(self):
        clear()
        caminho_arquivo = input('Digite o caminho do arquivo de texto: ')
        raiz = Pasta(self.nome)
    
        if not os.path.isfile(caminho_arquivo):
            clear()
            input(f'O caminho de arquivo "{caminho_arquivo}" não existe.\nPressione qualquer tecla para continuar.')
            raiz.inicio()
    
        raiz.criar_hierarquia_pastas(caminho_arquivo, raiz)
    
        print('Hierarquia de pastas criada com sucesso!\n')
    

    def main():
        clear()
        nome_pasta = input('Qual o nome da pasta Pai?\n')
    
        pastas = Pasta(str(nome_pasta))
        pastas.inicio()


    def __str__(self):
        return f'{self.nome}{self.filhos}'