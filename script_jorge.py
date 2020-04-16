import pandas as pd
import numpy as np

#abrindo o dataset
corona = pd.read_excel("diretório local com o .xlsx")

#fixando a coluna "Municipio" como index e convertendo as linhas em coluna, utilizando a função pivot
df = corona.pivot(index='Municipio', columns='Status', values='Total')

#removendo .0 do float
df['Diagnosticados'] = df['Diagnosticados'].apply(lambda f: format(f, '.0f'))
df['Mortes'] = df['Mortes'].apply(lambda f: format(f, '.0f'))
df['Suspeita'] = df['Suspeita'].apply(lambda f: format(f, '.0f'))

#substituindo valores NaN por 0
cols = ['Diagnosticados', 'Mortes', 'Suspeita']
df[cols] = df[cols].replace(['nan', 0], np.nan)
df[cols] = df[cols].fillna(0)

#resetando o índice município, para que se torne coluna
df.reset_index(level=0, inplace=True)
df.rename_axis(None, inplace=True)

#exportando para excel
df.to_csv(f'C:/Users/erick/Desktop/jorge/teste.csv',index=False, encoding='utf-8-sig')

#adicionando layer
layer_corona = QgsVectorLayer('diretório local com o .csv gerado', 'Corona', 'ogr')
QgsProject.instance().addMapLayer(layer_corona)

#setando o encoding UTF-8
uri.setProviderEncoding(u'UTF-8')
uri.dataProvider().setEncoding(u'UTF-8')

