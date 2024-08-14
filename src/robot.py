from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from artigo import Artigo

class Robot:
    def __init__(self,timeout=30):
        chrome_options = Options()
        chrome_options.add_argument("--no-first-run")  # Evitar a tela de boas-vindas
        chrome_options.add_argument("--no-default-browser-check")  # Evitar a verificação de navegador padrão
        # Inicializar o serviço do ChromeDriver
        service = Service(ChromeDriverManager().install())

        # Inicializar o driver do navegador com as opções configuradas usando o serviço configurado
        self.driver = webdriver.Chrome(service=service,options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout)  # Tempo de espera padrão de 30 segundos   

    def open(self,url):
        self.driver.get(url)

    def pegar_artigos(self):
        xpath = '//h2/a'
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        elementos = self.driver.find_elements(By.XPATH, xpath)
        artigos = []
        for elemento in elementos:
            titulo = elemento.text
            link = elemento.get_attribute("href")
            artigos.append(Artigo(titulo,link))
        return artigos
    
    def proxima_pagina(self):
        xpath = '//a[contains(text(),"Next")]'
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            elemento = self.driver.find_element(By.XPATH, xpath)
            elemento.click()
            return True
        except:
            return False
    
    def pegar_conteudo_artigo(self):
        xpath = '//div[@class="entry-content"]//p | //div[@class="entry-content"]//h2'
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        elementos = self.driver.find_elements(By.XPATH, xpath)
        texto = ""
        for elemento in elementos:
            texto += elemento.text + "\n"

        return 