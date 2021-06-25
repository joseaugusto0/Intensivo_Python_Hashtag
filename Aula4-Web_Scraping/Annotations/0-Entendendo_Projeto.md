# O que é Web Scraping
Web Scraping é a automação web, onde iremos entrar na internet, buscar informações, sites, preencher formulários, tudo de forma automatizada.

# Entendendo o Projeto
A nossa aplicação será uma automação que rodará em segundo plano, em paralelo a você usando o computador.
Vamos imaginar que trabalhamos em uma importadora que venda alguns produtos (presente no arquivo csv passado.)
Cada produto, portanto, é em uma moeda (Euro, Dolar e Ouro), temos que ter um preço final dos produtos de acordo com a cotação atual da moeda.
A nossa aplicação irá calcular esse preço final pegando a cotação das moedas na web, e atualizando o preço final no arquivo.
Iremos usar o Selenium pra isso

# Usando o Selenium
O Selenium é uma ferramenta que permite a automatização do navegador. Controlando ele por linhas de código.
Diferente do pyautogui, com o selenium, o código funcionará com quase todos os computadores (não depende de resolução igual do monitor pra uma automação no clique do mouse)

# Instalando o selenium
-   pip install selenium
-   Precisamos instalar o webdriver para fazer a conexão do python com o navegador
    -   No chrome, brave: chromedriver
    -   No firefox: gekodriver
    -   Iremos inserir esse arquivo no local de instalação do python
    -   Ou você pode passar o local do driver só (como estou usando uma env e o Brave Browser, foi o único jeito que consegui)
    ```
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

        chromedriver_loc = '../Archives/chromedriver'
        driver = webdriver.Chrome(options = options, executable_path=chromedriver_loc)
    ```