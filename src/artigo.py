class Artigo:
    conteudo = ""
    
    def __init__(self, titulo, link):
        self.titulo = titulo
        self.link = link
        
    def set_conteudo(self, conteudo):
        self.conteudo = conteudo

    def get_titulo(self):
        return self.titulo

    def get_link(self):
        return self.link

    def get_conteudo(self):
        return self.conteudo