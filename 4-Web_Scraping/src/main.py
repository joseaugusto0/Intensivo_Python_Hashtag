
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Faz essas configurações se está no Brave
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
#options.headless = True
chromedriver_loc = '../Archives/chromedriver'

#Abrindo o navegador
#Se você usou o driver direto, sem nenhuma env, não precisa desses parâmetros
navigator = webdriver.Chrome(options = options, executable_path=chromedriver_loc)

#Abrindo o navegador em uma página
navigator.get("https://google.com")

#Achando o elemento que digita a busca no google.com e digitando nele
navigator.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação dolar")

#Apertando Enter
navigator.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)

#Pegando a label com o valor do dólar no site
#Dentro da tag HTML da label, tem o valor como atributo (data-value), iremos pegar ele
cotacao_dolar = navigator.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")


# Entrando no google de novo, digitando "cotacao do euro" na barra de pesquisa e apertando enter
navigator.get("https://google.com")
navigator.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navigator.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#Obtendo a informação da cotação do euro
cotacao_euro = navigator.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

# Entrando no site melhorcambio, na parte da cotação do ouro
navigator.get("https://www.melhorcambio.com/ouro-hoje")

#Obtendo a informação da cotação do ouro
cotacao_ouro = navigator.find_element_by_xpath(
    '//*[@id="comercial"]').get_attribute("value").replace(",",".")

#Fechando o navegador
navigator.quit()

#Importando a tabela dos produtos
import pandas as pd 
tabel_dir = "../Archives/Produtos.xlsx"
tabel = pd.read_excel(tabel_dir)

#Atualizando a cotação
#Pegando quais linhas tem a moeda = "Dólar", e inserindo o valor em float na coluna "Cotação"
tabel.loc[tabel["Moeda"] == "Dólar","Cotação"] = float(cotacao_dolar)
tabel.loc[tabel["Moeda"] == "Euro","Cotação"] = float(cotacao_euro)
tabel.loc[tabel["Moeda"] == "Ouro","Cotação"] = float(cotacao_ouro)

#Atualizando o preço final
tabel["Preço Final"] = tabel["Preço Base Original"] * tabel["Cotação"]

#Exportando a tabela atualizada
new_tabel_dir = "../Archives/NewTabel.xlsx"
tabel.to_excel(new_tabel_dir, index=False)


