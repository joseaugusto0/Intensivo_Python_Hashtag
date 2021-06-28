# Passo a Passo para resolver o Projeto
-   1 - Pegar a cotação do dolar
-   2 - Pegar a cotação do Euro
-   3 - Pegar a cotação do Ouro
-   4 - Importar a lista de produtos
-   5 - Recalcular o preço de cada produto
-   6 - Salvar os novos preços dos produtos

# 1 Passo - Pegar a cotação do Dólar
-   Temos que abrir o navegador
```
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    #Faz essas configurações se está no Brave
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
    chromedriver_loc = '../Archives/chromedriver'

    #Caso você não queira que abra o navegador na tela, adiciona essa informação:
    options.headless=True

    #Abrindo o navegador
    #Se você usou o driver direto, sem nenhuma env, não precisa desses parâmetros
    driver = webdriver.Chrome(options = options, executable_path=chromedriver_loc)
```

-   Entrar na página web
Sempre tem que estar com o endereço completo (https, http)
```
    #Abrindo o navegador em uma página
    driver.get("https://google.com")
```

-   Digitar "cotação do dólar"
Temos que encontrar um elemento de inserção de texto (onde digitamos para pesquisar algo no google.com)
Para acharmos isso
    -   Entre no google pelo seu navegador
    -   Aperte F12
    -   Aperte CTRL+SHIFT+C (entrar no modo de inspeção)
    -   Clique no campo de pesquisa (Vai marcar o elemento HTML do campo de pesquisa)
    -   Clique com o botão direito em cima do HTML que ficou em azul
    -   Copy > Copy Xpath
```
    #Achando o elemento que digita a busca no google.com
    #Passamos o xPath para a função
    navigator.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação dólar")

    #Apertando Enter
    navigator.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").send_keys(Keys.ENTER)
```

-   Pegar a informação do valor do dólar
```
    #Pegando a label com o valor do dólar no site
    #Dentro da tag HTML da label, tem o valor como atributo (data-value), iremos pegar ele
    cotacao_dolar = navigator.find_element_by_xpath(
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
```

# 2 - Pegar a cotação do Euro

-  Entrando no google de novo, digitando "cotação euro" e apertando enter
``` 
    navigator.get("https://google.com")
    navigator.find_element_by_xpath(
        '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').send_keys("cotação euro")
    navigator.find_element_by_xpath(
        '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').send_keys(Keys.ENTER)
```

-   Pegando a informação de cotação
```
    cotacao_euro = navigator.find_element_by_xpath(
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
```

# 3 - Pegando a cotação do ouro

-  Entrando no melhorcambio
``` 
    navigator.get("https://www.melhorcambio.com/ouro-hoje")
```

-   Pegando a informação de cotação do ouro
```
    cotacao_ouro = navigator.find_element_by_xpath(
        '//*[@id="comercial"]').get_attribute("value").replace(",",".")
```

-   Fechando o navegador
```
    navigator.quit()
```

# 4 - Importando os dados dos produtos
Iremos importar a tabela dos produtos
```
    import pandas as pd 
    tabel_dir = "../Archives/Produtos.xlsx"
    tabel = pd.read_excel(tabel_dir)
```

# 5.1 - Atualizar a cotação
```
    tabel.loc[tabel["Moeda"] == "Dólar","Cotação"] = float(cotacao_dolar)
    tabel.loc[tabel["Moeda"] == "Euro","Cotação"] = float(cotacao_euro)
    tabel.loc[tabel["Moeda"] == "Ouro","Cotação"] = float(cotacao_ouro)
```
-   1º Parâmetro da função loc() -> Qual linha(s) localizar
-   2º Parametro da função loc() -> Qual coluna localizar

# 5.2 - Recalcular o Preço final
```
    tabel["Preço Final"] = tabel["Preço Base Original"] * tabel["Cotação"]
```

# 6 - Exportar a tabela atualizada
```
    new_tabel_dir = "../Archives/NewTabel.xlsx"
    tabel.to_excel(new_tabel_dir, index=False)
```
Na função to excel, iremos passar dois parâmetros:
-   1 - Diretório e o nome do arquivo a ser gerado
-   2 - Se iremos querer o index como uma coluna no arquivo