import os
def criar_pasta(pasta):
    if not os.path.exists(pasta):
        os.makedirs(pasta)
def deletar_pasta(pasta):
    if os.path.exists(pasta):
        os.rmdir(pasta)

def criar_artigo_txt(artigo):
    titulo = remover_caracteres_especiais(artigo.get_titulo())
    with open(f"artigos/{titulo}.txt", "w",encoding="utf-8") as file:
        file.write(artigo.get_conteudo())
        
def remover_caracteres_especiais(texto):
    return texto.encode("ascii", "ignore").decode("ascii")