# Primeira automação
Para aumentarmos a produtividade de uma função, iremos utilizar a automação no python.
Iremos automatizar o envio de um email diário que é enviado para um chefe de um comércio, contendo a quantidade de vendas no dia, um relatório.
Será criado uma RTA

# Configurar pausa entre comandos
Para que não ocorra problemas entre um comando e outro (por exemplo, por travamento de algo no PC), vamos usar uma pausa entre um comando e outro
```
    pyautogui.PAUSE = 1
```

# 1º - Abrir uma nova aba
Podemos usar o clique do mouse e do teclado para abrir uma nova aba no navegador.
Podemos clicar no "+" para abrir uma nova aba, ou apertar CTRL+T
Por praticidade iremos usar o CTRL+T

```
    # Vai simular o comando para apertar os botões CTRL+T
    pyautogui.hotkey('ctrl', 't')
```

# 2º - Digitar o endereço URL
Podemos usar um pyautogui.write(url_do_site) direto, porém pode dar um problema com o autocomplete do navegador, portanto, vamos usar o pyperclip para copiar o link, e colar de uma vez na barra de endereço:
```
    #Entrar no link do sistema
    url = "https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh"
    pyperclip.copy(url)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
```

# 3º - Entrando na pasta do Drive
Precisamos dar um duplo clique em cima da pasta desejada.
Nesse caso, iremos pegar a posição absoluta da pasta na tela e usar a ferramenta click do pyautogui
Isso é algo ruim do pyautogui, pois se trocar o monitor para um de resolução diferente, as coordenadas passadas já não irão apontar certo para a pasta no drive
```
    #Entrando na pasta no Drive
    time.sleep(2)
    pyautogui.click(367,269, clicks = 2)
    pyautogui.press('enter')
```

# 4º - Fazer download do arquivo
Iremos clicar com o botão direito, ir com o mouse até a opção "Fazer download" e apertar o botão direito
```
    #Fazendo download do arquivo
    time.sleep(2)
    pyautogui.click(367,269,button='right')
    pyautogui.click(494,638)
    time.sleep(10)
```

# 5º - Abrindo o arquivo baixado
Para abrir o arquivo .xlsx iremos utilizar a biblioteca do pandas para abrir esse tipo de arquivo

```
    dir = r"../Archives/Vendas - Dez.xlsx"
    tabel = pd.read_excel(dir)
    print(tabel)
```
O r'../Archives/...' o "r" vai dizer para o python que é um tipo padrão de escrita, sem se confundir nos caracteres especiais como "\"

# 6º - Calculando o faturamento de vendas
Iremos pegar a soma do valor total de vendas, com o preço e a quantidade
```
    #Calcular o faturamento da venda de produtos
    faturamento = tabela["Valor Final"].sum()
    quantidade = tabela["Valor Final"].sum()
```
A ferramenta sum() irá somar a coluna por inteiro

# 7º - Enviar o email
Temos de abrir uma nova aba, entrar no site do gmail, clicar para escrever um novo email, escrever o email, o remetente, o assunto, o texto, e clicar em enviar

## 7.1 - Entrar no gmail
```
    url_email = "gmail.com"
    pyautogui.hotkey('ctrl', 't')
    pyperclip.copy(url_email)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep(7)
```

## 7.2 - Gerando a estrutura do email
```
    pyautogui.click(61,167)     #Clicar no botão "Escrever"
    pyautogui.write(destinatario)     #Digitar o email que vai ser enviado o email
    pyautogui.press('tab')          #O primeiro tab vai confirmar o email digitado
    pyautogui.press('tab')          #O segundo tab vai para o próximo bloco, no caso, do Assunto
    pyautogui.write(assunto)        #Vai digitar o assunto 
    pyautogui.press('tab')          # Vai para o bloco do corpo da mensagem
```

## 7.3 - Gerando o corpo do email
```
    text = "Olá,\nsegue o faturamento do dia: \n\n"
    text += f"Faturamento: R${faturamento}\n"
    text += f"Quantidade vendida: {quantidade} produtos\n"
    text += "\n\n"
    text += "Atenciosamente, Zé"
    pyperclip.copy(text)
```

## 7.4 - Inserindo o corpo da mensagem e enviando o email
```
    pyautogui.hotkey('ctrl','v')    #Vai colar o corpo do email
    pyautogui.hotkey('ctrl','enter')    #O gmail tem uma hotkey para enviar direto o email, no caso Ctrl+enter
```

