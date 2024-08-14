from robot import Robot
from utils import fileutils
from dotenv import load_dotenv
import os
def main():
    
    try:
        # Carregar variáveis de ambiente do arquivo .env
        load_dotenv()
        robot = Robot(timeout=10)
        nome_pasta = os.getenv("NOME_PASTA")
        fileutils.deletar_pasta()
        fileutils.criar_pasta()
        url_artigos = os.getenv("URL_ARTIGOS")
        robot.open(url_artigos)
        artigos =  []
        while True:
            artigos.append(robot.pegar_artigos())  
            proxima_pagina = robot.proxima_pagina()
            if not proxima_pagina:
                break

        for artigo in artigos:
            for a in artigo:
                print(f"Titulo: {a.get_titulo()}")
                print(f"Link: {a.get_link()}")
                robot.open(a.get_link())
                a.set_conteudo(robot.pegar_conteudo_artigo())
                fileutils.criar_artigo_txt(a)
            

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        robot.driver.quit()   


if __name__ == "__main__":
    main()

    