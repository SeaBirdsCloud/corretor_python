from Corretor_Class import Corretor


opcao = input("Deseja mudar o arquivo? (S/N) ")
if opcao == "S" or opcao == "s":
    arquivo = input("Digite o nome do arquivo: ")

artigos = Corretor.AbrirArquivo("artigos.txt")
