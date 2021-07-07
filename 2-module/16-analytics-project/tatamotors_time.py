# %%
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


# %%
# https://in.finance.yahoo.com/quote/TATAMOTORS.NS/history?p=TATAMOTORS.NS
data = pd.read_csv('./datasets/tatamotors.csv')
data.head()

# %%
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day

# %%
data.rename(columns={'Adj Close': 'Price'}, inplace=True)
data.head()

# %%
# selecting data to work
data_temp = data.loc[data['Year'] > 2018, ['Date', 'Price']]
data_temp.shape

# %%
data_temp['Date'].min(), data_temp['Date'].max()

# %%
data_grp = data_temp.groupby(['Date'], as_index=True).mean()
data_grp.head(5)

# %%
df_indx = data_grp.Price.resample('MS').mean()
df_indx.head(10)

df = data_grp.Price.resample('MS').mean().reset_index()
df.head(10)

# %%%
# df.plot utiliza el indice de fecha para graficar
fig = plt.figure(facecolor='w')
df_indx.plot(figsize=(15, 6), marker="o", markersize=10, markerfacecolor='red')

# %%
import statsmodels.api as sm
matplotlib.rcParams['figure.figsize']=11,8
decomposition = sm.tsa.seasonal_decompose(df_indx, model = 'additive')
fig = decomposition.plot()
plt.show()

# %%
from statsmodels.tsa.stattools import adfuller
print('Los datos son estacionarios?')
df_test = adfuller(df.Price, autolag = None)
print(f'Prueba estadistica{df_test[0]}')
print(f'P-value={df_test[1]}')
print(f'Valores criticos:')
for k, v in df_test[4].items():
    print('\t{}:{} Los datos son {} estacionarios con {}% de confianza'.format(k, v, "not" if v < df_test[0] else "", 100-int(k[:-1])))
    
# %%
import itertools 
p = d = q = range(0,2)
# AIC(Arkaike Information Criteria)
# Este estimador nos permite encontrar los mejores parámetros para Sarimax
pdq = list(itertools.product(p,d,q))
seasonal_pdq = [(x[0],x[1],x[2],12) for x in list( itertools.product(p,d,q))]
print(f'Sarimax: {pdq[1]} x {seasonal_pdq[1]}')
# %%
for param in pdq:
  for param_estacional in seasonal_pdq:
    try:
      mod= sm.tsa.statespace.SARIMAX(
          df_indx,
          order=param,
          seasonal_order=param_estacional,
          enforce_stationarity = False
      )
      results = mod.fit()
      print(f'ARIMA {param} x {param_estacional}12 - AIC:{results.aic}')
    except:
      continue
  
# %%
mod= sm.tsa.statespace.SARIMAX(
          df_indx,
          order=(0, 0, 1),
          seasonal_order=(0, 0, 1, 12),
          enforce_stationarity = False
      )
resultados = mod.fit()
# %%
resultados.plot_diagnostics(figsize=(16,8))
plt.show()
# %%
predicciones = resultados.get_prediction(start=pd.to_datetime('2019-01-01'))
pred_conf_int = predicciones.conf_int()
pred_conf_int

# %%
ax = df_indx['2019':].plot(label='Observados')
predicciones.predicted_mean.plot(ax=ax, label ='Pronostico futuro', alpha =.7, figsize=(14,7))
ax.fill_between(pred_conf_int.index,
                pred_conf_int.iloc[:,0],
                pred_conf_int.iloc[:,1],
                color='gray',
                alpha=.2)
plt.legend()
plt.show()

# %%
prediccion_futurista = resultados.get_forecast(steps=50)
pred_ci=prediccion_futurista.conf_int()
ax = df_indx.plot(label='Pasado')
prediccion_futurista.predicted_mean.plot(ax=ax, label ='Pronostico', alpha =.7, figsize=(14,7))
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:,0],
                pred_ci.iloc[:,1],
                color='gray',
                alpha=.2)
plt.legend()
plt.show()
# %%
