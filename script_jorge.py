import pandas as pd
import numpy as np

#Abrindo o dataset
corona = pd.read_excel("diretório local com o .xlsx")

#Fixando a coluna "Municipio" como index e convertendo as linhas em coluna, utilizando a função pivot
df = corona.pivot(index='Municipio', columns='Status', values='Total')

#Substituindo valores NaN por 0
cols = ['Diagnosticados', 'Mortes', 'Suspeita']
df[cols] = df[cols].replace(['nan', 0], np.nan)
df[cols] = df[cols].fillna(0)

#Transformando para tipo inteiro
df[list(cols)] = df[list(cols)].fillna(0.0).astype(int)

#Resetando o índice município, para que se torne coluna
df.reset_index(level=0, inplace=True)
df.rename_axis(None, inplace=True)

#Exportando para excel
df.to_csv(f'diretório local apontando o salvamento do .csv',index=False, encoding='utf-8-sig')

#Adicionando como layer no QGIS
layer_corona = QgsVectorLayer('diretório local com o .csv gerado', 'Corona', 'ogr')
QgsProject.instance().addMapLayer(layer_corona)

#Setando o encoding UTF-8 para a tabela no QGIS
layer_corona.setProviderEncoding(u'UTF-8')

