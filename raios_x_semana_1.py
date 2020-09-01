import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_intensidade = pd.read_csv('eq17_35kV-30graus.txt', sep='\t')
df_variacao_tensao = pd.read_csv('eq17_variaçãotensão.txt', sep='\t')

tetas_intensidade = df_intensidade['teta']
fig, ax = plt.subplots()
g1 = plt.plot(tetas_intensidade, df_intensidade['IM1/s'], label='IM1/s')
g2 = plt.plot(tetas_intensidade, df_intensidade['IM2/s'], label='IM2/s')
plt.xticks(rotation=45)
every_nth = 10
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
plt.legend()
plt.xlabel('Theta (graus)')
plt.ylabel('Intensidade (fótons/s)')
plt.show()

tetas_variacao = df_variacao_tensao['teta']
fig, ax = plt.subplots()
tensao1 = plt.plot(tetas_variacao, df_variacao_tensao['35kV/s'],label='35kV/s')
tensao2 = plt.plot(tetas_variacao, df_variacao_tensao['30kV/s'],label='30kV/s')
tensao3 = plt.plot(tetas_variacao, df_variacao_tensao['28kV/s'],label='28kV/s')
tensao4 = plt.plot(tetas_variacao, df_variacao_tensao['25kV/s'],label='25kV/s')
tensao5 = plt.plot(tetas_variacao, df_variacao_tensao['18kV/s'],label='18kV/s')
plt.xticks(rotation=45)
every_nth = 3
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
plt.legend()
plt.xlabel('Theta (graus)')
plt.ylabel('Intensidade (fótons/s)')
plt.show()