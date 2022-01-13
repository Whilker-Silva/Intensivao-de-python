# Tratamento de dados (Corrigir os problemas da base de dados)
# Análise inicial
# Análise dethalada dos clientes

import pandas as pd
import plotly.express as px

# Importar a base de dados
tabela = pd.read_csv(
    r"C:\Users\whilk\Documents\VsCode\Curso de python\telecom_users.csv")

# Tratamento de dados (Corrigir os problemas da base de dados)
# Coluna inúltil
# Valores reconhecidos de forma errada
# Tratar valores vazios


# axis = 0 -> lihhacle
# axis = 1 -> coluna
tabela = tabela.drop("Unnamed: 0", axis=1)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())
print()
print("_____________________________________________________________")
print()
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")

grafico.show()