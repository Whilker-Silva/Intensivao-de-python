# Tratamento de dados (Corrigir os problemas da base de dados)
# Análise inicial
# Análise dethalada dos clientes

import pandas as pd

# Importar a base de dados
tabela = pd.read_csv(r"C:\Users\whilk\Desktop\telecom_users.csv")

# Tratamento de dados (Corrigir os problemas da base de dados)
# Coluna inúltil
# Valores reconhecidos de forma errada
# Tratar valores vazios


# axis = 0 -> lihhacle
# axis = 1 -> coluna
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)


