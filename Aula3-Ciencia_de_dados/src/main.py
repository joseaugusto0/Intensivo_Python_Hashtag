import pandas as pd

csv_dir = "../Archives/advertising.csv"

#Importando a base de dados
tabel = pd.read_csv(csv_dir)

#Observando e tratando os dados
#print(tabel)
#print(tabel.info())
#No nosso caso, a tabela já está bem estruturada, só tem um detalhe 
#das vendas estarem em uma unidade diferente das outras coluna, porém podemos ajustar isso mais pra frente

#Analise Exploratória
#Exibindo a correlação das informações  
import seaborn as sns
import matplotlib.pyplot as plt
#sns.heatmap(tabel.corr(), annot=True)
#plt.show()

#Separando os dados em teste/treino
from sklearn.model_selection import train_test_split

y = tabel["Vendas"]
x = tabel.drop("Vendas", axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

# Gerando a regressão linear
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

#Criando os modelos das IA's
modelo_linearRegression = LinearRegression()
modelo_randomForestRegression = RandomForestRegressor()

#Treina as inteligências
modelo_linearRegression.fit(x_treino, y_treino)
modelo_randomForestRegression.fit(x_treino, y_treino)

# Checando a eficácia da IA
from sklearn import metrics

#Criar as previsões
predict_linearRegression = modelo_linearRegression.predict(x_teste)
predict_randomForestRegression = modelo_randomForestRegression.predict(x_teste)

#Comparando os modelos
print(metrics.r2_score(predict_linearRegression,y_teste))
print(metrics.r2_score(predict_randomForestRegression,y_teste))

#Visualizar graficamente os predicts
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["RandomForestRegressionPredict"] = predict_randomForestRegression
tabela_auxiliar["LinearRegressionPredict"] = predict_linearRegression
#sns.lineplot(data=tabela_auxiliar)
#plt.show()

#Analisar importancia de cada variável para as vendas
sns.barplot(x=x_treino.columns, y=modelo_randomForestRegression.feature_importances_)
plt.show()