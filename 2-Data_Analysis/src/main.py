import pandas as pd
import plotly.express as px

#Importando a tabela
dir_tabel = "../Archives/telecom_users.csv"
tabel = pd.read_csv(dir_tabel)

#Checar as informações da tabela
#print(tabel.info())

#Deletar a primeira coluna inútil
tabel = tabel.drop("Unnamed: 0", axis=1)

#Convertendo a tabela Total Gasto de texto para números
tabel["TotalGasto"] = pd.to_numeric(tabel["TotalGasto"], errors="coerce")


#Excluindo as colunas vazias
tabel = tabel.dropna(how="all", axis=1)

#Excluindo as linhas que possuem algum dado vazio
tabel = tabel.dropna(how="any", axis=0)

#Analisando a coluna que mostra o cancelamento
#Iremos pegar os valores de Sim ou Não na tabela em porcentagem
print(tabel["Churn"].value_counts(normalize=True))

#Mostrando um gráfico de histograma analisando a coluna MesesComoCliente em relação a coluna Churn
#Será gerado um gráfico em HTML
#grafico = px.histogram(tabel, x="MesesComoCliente", color="Churn")
#grafico.show()

#Para analisarmos todas as colunas em relação a coluna Churn, iremos usar um for
for column in tabel:
    if column!="Churn":
        grafico = px.histogram(tabel,x=column, color="Churn")
        grafico.show()







