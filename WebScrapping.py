from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

edge_options = Options()
edge_options.add_argument('--headless')  # Roda sem abrir o navegador
edge_options.add_argument('--disable-gpu')
edge_options.add_argument('--no-sandbox')

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=edge_options)

caminho = "https://www.amazon.com.br/s?k=monitor+27+polegadas&crid=2BXGDPJX7837C&sprefix=mON%2Caps%2C342&ref=nb_sb_ss_ts-doa-p_4_3"

driver.get(caminho)
elem = driver.find_elements(By.TAG_NAME, "h2")
elem_2 = driver.find_elements(By.TAG_NAME, "a-price-whole")


for h2 in elem_2:
    print(h2.text)
driver.quit()
