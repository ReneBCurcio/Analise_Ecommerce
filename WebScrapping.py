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
elem = driver.find_element(By.CSS_SELECTOR, "h2")
print(elem)

driver.quit()
