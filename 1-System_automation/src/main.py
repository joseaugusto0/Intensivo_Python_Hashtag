import pyautogui
import time
import pyperclip
import pandas as pd

url = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"
url_email = "http://gmail.com/"
destinatario = "twentygamer@gmail.com"
assunto = "Envio de relatório"
pyautogui.PAUSE = 0.5

time.sleep(2)

#Abrir uma nova aba
pyautogui.hotkey('ctrl', 't')

#Abrir um navegador do zero
#pyautogui.press('win')
#pyautogui.write('brave')
#pyautogui.press('enter')


#Entrar no link do sistema
pyperclip.copy(url)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

#Entrando na pasta no Drive
#time.sleep(2) //Isso aqui foi usado para pegarmos o valor exato da posição da pasta no navegador
#print(pyautogui.position())
time.sleep(2)
pyautogui.click(367,269, clicks = 2)
pyautogui.press('enter')

#Fazendo download do arquivo
time.sleep(1)
pyautogui.click(367,269,button='right')
#pyautogui.click(494,638)
#time.sleep(1)

#Abrindo o arquivo baixado
dir = r"../Archives/Vendas - Dez.xlsx"
tabel = pd.read_excel(dir)

#Calcular o faturamento da venda de produtos
faturamento = tabel["Valor Final"].sum()
quantidade = tabel["Valor Final"].sum()


#Entrando no Gmail
pyautogui.hotkey('ctrl', 't')
pyperclip.copy(url_email)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(7)

# Criando um novo email a ser enviado
pyautogui.click(61,167)
pyautogui.write(destinatario)
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')

# Gerando o corpo da mensagem
text = "Olá,\nsegue o faturamento do dia: \n\n"
text += f"Faturamento: R$ {faturamento}\n"
text += f"Quantidade vendida: {quantidade} produtos\n"
text += "\n\n"
text += "Atenciosamente, Zé"
pyperclip.copy(text)

#Terminando o email e enviando-o
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('ctrl','enter')




