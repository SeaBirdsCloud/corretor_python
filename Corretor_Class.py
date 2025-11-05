import nltk
nltk.download('punkt')

class Corretor:
    def __init__(self):
        pass

    def AbrirArquivo(self, arquivo):
        arquivo = arquivo.replace(" ", "")
        arquivo = open(arquivo, 'r')
        with open(arquivo, "r", encoding="utf-8") as f:
            artigos = f.read()
        print(artigos[:500])
