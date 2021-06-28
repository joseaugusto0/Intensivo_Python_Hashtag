# 1º Passo - Importar a base de dados
Iremos usar o pandas para importar a tabela
```
    import pandas as pd

    dir_tabel = "../Archives/telecom_users.csv"
    tabel = pd.read_csv(dir_tabel)
```

# 2º Passo - Visualizar a base de dados
Aqui iremos observar quais informações não fazem sentido, ou estão faltando, ou estão em outro formato, etc.
-   Ver se os dados numéricos estão lidos como números, e não como texto!
-   1ª coluna ('Unnamed') é uma coluna com nome aleatório, que apresenta número supostamente aleatórios = temos que removê-la
-   Coluna "código" está com valores NaN = temos que tratar esses valores vazios

# 3º Passo - Tratamento de dados
## 3.1 - Deletando a coluna inútil
```
    tabel = tabel.drop("Unnamed: 0", axis=1)
```
Aqui irá pegar a tabela importada anteriormente, e a coluna chamada "Unnamed" vai ser deletada. O parâmetro axis dirá que o drop será de uma coluna (1), caso fosse uma linha, o valor seria 0

## 3.2 - Checando se os dados numéricos estão sendo lidos como números
```
    print(tabel.info())
```
Essa função irá mostrar algumas informações da tabela, nos atentaremos as seguintes: Listará as colunas uma por uma, mostrando o número de linhas não vazias de cada uma, e o tipo de cada uma.
O pandas, por padrão, se vê uma coluna com texto, irá dizer que a coluna é do tipo **object**
Observamos que a coluna de Total Gasto está sendo lida como texto

## 3.3 - Convertendo a coluna TotalGasto de object(texto) para número
```
    tabel["TotalGasto"] = pd.to_numeric(tabel["TotalGasto"], errors="coerce")
```
A função to_numeric irá pegar a coluna e fazer a conversão para um dado númerico.
O parâmetro errors="coerce" irá dizer para caso ocorra algum erro em alguma linha durante a conversão (como por exemplo, tentar converter uma letra para um número), ele irá deixar aquela linha vazia

## 3.4 - Resolver as colunas vazias
Temos que primeiro resolver as colunas vazias, pois se tentarmos excluir as linhas que possui algum dado vazio, e houver uma coluna vazia, ele vai excluir a tabela inteira
```
    tabel = tabel.dropna(how="all", axis=1)
```
Essa função já irá analisar a tabela e excluir as linhas/colunas com valores vazios, de acordo com o parâmetros passado
-   how -> Irá dizer se queremos excluir a linha/coluna se todos os dados forem vazios (how="all"), ou se queremos excluí-la se um ou mais valores forem vazio (how="any")

## 3.5 - Resolver as linhas com valores vazios
Como temos um database com quase 6000 linhas, e apenas umas 12 linhas estão com valores vazios, podemos excluir essas linhas que não terá tanto impacto na análise
```
    tabel = tabel.dropna(how="any", axis=0)
```

# 4º Passo - Análise dos dados
## Analisar a coluna vinculada ao cancelamento = coluna "Churn"
```
    print(tabel["Churn"].value_counts(normalize=True))
```
O value counts vai te mostrar os diferentes valores presente na coluna, e a quantidade que é repetida desses valores na mesma coluna.
O parâmetro normalize=True irá gerar a quantidade de valores repetidos na coluna no valor de porcentagem, caso não seja passado esse parâmetro, ele irá mostrar o valor inteiro de repetições de valores.

# 5º Passo - Analisar características que influenciam o cancelamento
## 5.1 - 1ª Hipótese - Relacionar os meses de cadastro dos clientes com o número de cancelamento
Vamos analisar a interligação entre colunas, por exemplo, observar dos que cancelaram, quantos meses eles já tinham de cadastro
O melhor jeito de observarmos isso é usar gráficos com o plotly.express
```
    import plotly.express as px

    grafico = px.histogram(tabel, x="MesesComoCliente", color="Churn")
    grafico.show()
```
Com esse código, iremos criar um histograma (em HTML) com os três parâmetros passados:
-   1º parametro: De qual tabela queremos pegar os dados
-   2º parâmetro: Nome da coluna (presente na tabela passada) que queremos inserir no eixo x
-   3º parâmetro: Qual coluna (presente na tabela passada) você quer que separe por cores

## 5.2 - Analisar todas as colunas de forma automatizada
Para que não precisemos analisar tabela por tabela em relação ao cancelamento, iremos utilizar uma forma mais automática pra realizar isso.
Iremos usar um for para analisar todas as colunas
```
    for column in tabel:
        if column!="Churn":
            grafico = px.histogram(tabel,x=column, color="Churn")
            grafico.show()
```
A variável column conterá apenas o nome de cada coluna
Caso coloquemos "for line in tabel.index", ele irá ir de linha em linha

## 6º Passo - Conclusões
Iremos analisar os gráficos para coisas que chamem a atenção, que apontem a algum problema visível que possa ocorrer o cancelamento
-   Cancelamento por gênero = Praticamente número igual de cancelamentos (Descartado)
-   Cancelamento se o cliente é aposentado - Proporção quase igual (Descartado)
-   Cancelamento se o cliente é casado - Há um pouco mais de cancelamentos de clientes que não são casados. Mas é uma informação que não tem muito o que tirar de mais. (Descartado)
-   Cancelamento se o cliente tem dependente - Proporção de cancelamento é maior para clientes sem dependentes.
-   Cancelamento de acordo com os meses de cadastro do cliente - Há um maior número de cancelamento de clientes com menos de 10 meses de cadastro
    -   Possivelmente há um problema na retenção de cliente nos primeiro meses
    -   Podemos criar um programa para incentivar os clientes nos primeiros meses
    -   Talvez a captação de clientes não foi feita de forma correta
-   Cancelamento se o cliente tem serviço de internet - Maior cancelamento dos clientes que utilizam a Fibra
    -   Há um problema na internet com fibra ótica
-   Cancelamento se o cliente tem mais serviços - Quando o cliente tem mais serviços, menor é a porcentagem de cancelamento dele
    -   Temos que criar um programa de incentivo a contratação de mais serviços, mesmo que o preço tenha que cair drasticamente
-   Cancelamento pelo tipo de contrato com o cliente - Clientes com contrato mensal tendem a cancelar mais
    -   Incentivar o cliente ao contrato anual (como por exemplo, descontos)
-   Cancelamento pelo tipo de pagamento - Cliente com pagamento por boleto eletrônico cancela mais
    -   Incentivar outro método de pagamento



  
