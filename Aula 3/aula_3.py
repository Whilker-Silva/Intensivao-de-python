#importando bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import pandas as pd

#criando navegado webdriver e abrindo pagina do google
navegador = webdriver.Chrome(r"Aula 3\chromedriver.exe")
navegador.get("https://www.google.com/")

#1 cotação do dolar
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys("cotação dolar")
pyautogui.press("enter")
dolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

#2 cotação do euro
navegador.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[2]/div/div[2]/input').clear()
navegador.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[2]/div/div[2]/input').send_keys("cotação euro")
pyautogui.press("enter")
euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

#3 cotatção do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
ouro = ouro.replace(",", ".")

#fechando navegador
navegador.quit()

#4 importar e atualizar a base de dados
tabela = pd.read_excel(r"Aula 3\Produtos.xlsx")
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(dolar)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(euro)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(ouro)

#5 calcular os preços 
tabela["Preço de Compra"] = tabela["Preço Original"]*tabela["Cotação"]
tabela["Preço de Venda"] = tabela["Preço de Compra"]*tabela["Margem"]

#6 salvar a base de dados
tabela.to_excel("Produtos_novo.xlsx", index=False)

print(dolar)
print(euro)
print(ouro)
print()
print(tabela)