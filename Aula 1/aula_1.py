import pyautogui
import pyperclip
import time
import pandas as pd





#definindo pausa geral para cada ação do pyautogui
pyautogui.PAUSE = 0.3

#abrir google chrome
pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

#Abrir link e pasta do arquivo
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(4)
pyautogui.click(x=1774, y=270, clicks=2)
time.sleep(3)

#Fazer Donwload
pyautogui.click(x=1703, y=309)
pyautogui.click(x=2759, y=164)
pyautogui.click(x=2532, y=600)
time.sleep(5)

#importar base de dados para python
tabela = pd.read_excel(r"C:\Users\whilk\Downloads\Vendas - Dez.xlsx")
#print(tabela)

#Calcular faturamento e quantidade de produtos vendidos 
faturamento = tabela["Valor Final"].sum()
qtd_produtos = tabela["Quantidade"].sum()
#print(faturamento)
#print(qtd_produtos)

#Acessar guia anônima e acessar outlook
pyautogui.hotkey("ctrl", "shift", "n")
pyperclip.copy("https://outlook.live.com/owa/")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

#Fazer login
pyautogui.click(x=2589, y=95)
time.sleep(2)

pyperclip.copy("whilker_santos@hotmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(2)

pyperclip.copy("23n2001whss")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=2193, y=556)
time.sleep(8)

#Escrever e-mail
pyautogui.click(x=1523, y=175)
time.sleep(2)
pyperclip.copy("whilker.ml@hotmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
pyperclip.copy("Relatório de vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

#corpo do e-mail
texto = f"""
Bom dia!

Segue valor em vendas do dia de ontem.

Faturamento: R${faturamento:,.2f}
Quantidade de vendas: {qtd_produtos}

Abs
Whilker Henrique.
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")
















