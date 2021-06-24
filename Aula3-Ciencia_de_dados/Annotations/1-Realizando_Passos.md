# 1- Importando os dados
Importaremos a tabela com o **pandas**
```
    import pandas as pd

    csv_dir = "../Archives/advertising.csv"
    tabel = pd.read_csv(csv_dir)
```

# 2 - Ajuste de Dados/Tratamento
Nossa tabela tem colunas para o valor gasto para publicação em TV, em Rádio, em Jornal, e o quanto isso resultou em Vendas.
Porém, as colunas TV, rádio e jornal estão em unidadesX1000, enquanto as vendas estão em unidades*1000000
Mas isso podemos resolver mais pra frente

# 3 - Análise exploratória
Temos que analisar as correlações entre as informações dadas
Vamos analisar a correlação de TV com as vendas, do Rádio com as vendas, e o jornal com as vendas.
Por exemplo, o investimento em TV é proporcionalmente ao aumento de vendas (entre um valor de -1 e 1)
Para fazer essa correlação, iremos usar os mapas de calor do seaborn
```
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.heatmap(tabel.corr(), annot=True)
    plt.show()
```
O seaborn é feito em conjunto com o matplotlib, então se importar ele, tem de importar o matplotlib.
tabel.corr() irá dizer que é a correlação entre as tabelas
O annot=True só irá colocar os valores de correlação direto no gráfico
-   Observamos que a correlação entre o investimento na TV e as vendas é de 0.9
-   Observamos que a correlação entre o investimento na rádio e jornal e as vendas é de 0.35 ambas
-   A correlação entre as colunas de investimento não podem ser altas, pois podem dificultar a análise de vendas
    -   Imagine que o investimento de rádio e TV fossem altos, o investimento de TV ia afetar diretamente o de rádio, e não agiriam como "variáveis independentes"

# 4 - Separar as nossas informações entre dados de treino e de teste (Machine Learning)
No nosso caso, iremos utilizar os dados de treino para treinar nossa IA, e os dados de teste para verificar se a IA realmente está eficaz
```
    #Separando os dados em teste/treino
    from sklearn.model_selection import train_test_split

    y = tabel["Vendas"]
    x = tabel.drop("Vendas", axis=1)

    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)
```
X são os dados que usaremos para obter a previsão (investimento em TV, Rádio e jornal)
Y são os dados que tentaremos prever (vendas)
O test_size vai dizer que queremos apenas 30% dos nossos dados sendo utilizados para teste
Os valores de treino são superiores aos de teste.
O random_state=1 vai dizer que iremos escolher os dados de forma aleatória apenas uma vez, se rodarmos o código de novo, ele vai pegar a mesma separação de dados feito anteriormente

# 5 - Gerando uma regressão para o nosso caso
-   Podemos utilizar a regressão linear com os nossos dados
-   Podemos utilizar também a RandomForest (Árvore de Decisão)
```
    # Gerando a regressão linear
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestRegressor

    #Criando os modelos das IA's
    modelo_linearRegression = LinearRegression()
    modelo_randomForestRegression = RandomForestRegressor()

    #Treina as inteligências
    modelo_linearRegression.fit(x_treino, y_treino)
    modelo_randomForestRegression.fit(x_treino, y_treino)
```

# 6 - Testando a Regressão feita
Vamos usar o R^2 -> % de acerto da nossa IA
```
    # Checando a eficácia da IA
    from sklearn import metrics

    #Criar as previsões
    predict_linearRegression = modelo_linearRegression.predict(x_teste)
    predict_randomForestRegression = modelo_randomForestRegression.predict(x_teste)

    #Comparando os modelos
    print(metrics.r2_score(predict_linearRegression,y_teste))
    print(metrics.r2_score(predict_randomForestRegression,y_teste))
```
A previsão do Árvore de decisão foi de 96,13% no meu computador, enquanto a de regressão linear foi de 90,09%

# 7 - Visualização gráfica das previsões
Vamos criar um gráfico de linhas com o y_teste, e os predict da arvore de decisão e da regressão linear, para que consigamos ver o quanto as linhas de predict estão próximas do y_teste
```
    #Visualizar graficamente os predicts
    tabela_auxiliar = pd.DataFrame()
    tabela_auxiliar["y_teste"] = y_teste
    tabela_auxiliar["RandomForestRegressionPredict"] = predict_randomForestRegression
    tabela_auxiliar["LinearRegressionPredict"] = predict_linearRegression

    sns.lineplot(data=tabela_auxiliar)
    plt.show()
```

# 8 - Importancia de cada variável para as vendas
Precisamos analisar a influência de cada variável de investimento no valor final das vendas obtidas, segundo o modelo
```
    #Analisar importancia de cada variável para as vendas
    sns.barplot(x=x_treino.columns, y=modelo_randomForestRegression.feature_importances_)
    plt.show()
```

# 9 - Conclusões
-   Observamos que a TV tem um retorno maior de vendas (1º lugar) do que a Rádio (2º lugar), e do que o jornal (3º lugar)
-   Logo, podemos afirmar que o investimento em TV é muito mais assertivo que o do Jornal








