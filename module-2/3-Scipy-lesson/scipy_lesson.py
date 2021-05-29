# %%
import pandas as pd
import numpy as np
import math

# %% [markdown]
# # None (Not a Number)
# ## dato desconocido, un dato desconocido no es igual a otro dato desconocido

# %%
np.nan == np.nan
a = np.nan
b = np.nan
a == b

# %% 
print(id(a), id(b))

# %%
type(a)
# %%
c = math.nan
d = math.nan
print(c==d)
print(id(c),id(d))
# %%
e=float('nan')

# %%
# isnull trata cualquier tipo de nan como nulo
print(pd.isnull(a), pd.isnull(b), pd.isnull(e))

# %%
def llenar_lista_con_2(lista =[], numero=0):
    print(id(lista), id(numero))
    lista.append(2)
    numero += 2
    print(id(lista), lista(numero))
    print(lista, numero)

# %%
llenar_lista_con_2
# %%
def llenar_lista_con_2(lista = None, numero=0):
    if lista == None:
        lista = []
    print(id(lista), id(numero))
    lista.append(2)
    numero += 2
    print(id(lista), lista(numero))
    print(lista, numero)

# %%
llenar_lista_con_2

# %%
import statistics
import scipy
import pandas as pd
import numpy as np

# %%
x = [1,2,3,4,5,6]
x_nan = [1,2,3,np.nan,5,6]

# %%
arr = np.array(x)
arr_nan = np.array(x_nan)

# %%
ser = pd.Series(x)
ser_nan = pd.Series(x_nan)

# %%
statistics.fmean(arr)
todos = {'lista': x, 'lista_nan': x_nan, 'array': arr, 'array_nan': arr_nan,
         'serie': ser, 'serie_nan': ser_nan}

# %%
for key, val in todos.items():
  print(key)
  print(val)

# %%
for key, val in todos.items():
  print(key)
  print(sum(val)/len(val))
# %%
for key, val in todos.items():
  print(key)
  print(statistics.mean(val))
# %%
int(sum(arr)/len(arr))
# %%
for key, val in todos.items():
  print(key)
  print(np.mean(val))
# %%
ser_nan
# %%
(1+2+3+5+6)/5

# %%
(1+2+3+4+5+6)/6
# %%
for key, val in todos.items():
  print(key)
#  print(scipy.mean(val))
# %%
for key, val in todos.items():
  print(key)
  print(np.nanmean(val))
# %%
def mediana_python(objeto):
  n = len(objeto)
  if n%2 != 0:
    mediana = sorted(objeto)[int((n-1)*0.5)]
  else:
    ob_ord = sorted(objeto)
    ind = int(n*0.5)
    mediana = (ob_ord[ind] + ob_ord[ind-1])/2
  return mediana

# %%
mediana_python([1,5,2,np.nan,2,3,4,5])

# %%
sorted([1,6,5,np.nan,2,3,4,5])
# %%
sorted(x_nan)
# %%
for key, val in todos.items():
  print(key)
  print(statistics.median(val))
# %%
# regresa solo el nan
for key, val in todos.items():
  print(key)
  print(np.median(val))
# %%
np.median([1,5,2,np.nan,2,3,4,5])
# %%
# ignorar el nan
for key, val in todos.items():
  print(key)
  print(np.nanmedian(val))

# %%
ser.median()
# %%
ser_nan.median()
# %%
ser_nan.median(skipna = False)

# %%
u = [1,2,3,1,6,1,7,1,54]
v = [1,2,1,2,1,2,6,1,87,432]

# %%
[(u.count(elemento), elemento) for elemento in set(u)]

# %%
max([(u.count(elemento), elemento) for elemento in set(u)])

# %%
[(v.count(elemento), elemento) for elemento in set(v)]
# %%
max([(v.count(elemento), elemento) for elemento in set(v)])
# %%
statistics.mode(u)
# %%
statistics.median(v)
# %%
#scipy.stats.mode(u)
# %%
j = [2, np.nan, np.nan, np.nan, np.nan, np.nan]
j2 = [1,1, np.nan]

# %%
max([(j.count(elemento), elemento) for elemento in set(j)])
# %%
statistics.mode(j2)
# %%
# scipy.stats.mode(j2)
# %%
u,v,j,j1 = pd.Series(u),pd.Series(v),pd.Series(j),pd.Series(j2)
# %%
u.mode()
# %%
v.mode()
# %%
j.mode()
# %%
j1.mode()
# %% [markdown]
# ## combinaciones, permutaciones y exponenciales
# ## scipy.special

# %%
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# %%

# %%
x = [1,2,3,4,5]
stats.describe(x)

# %%
normal = stats.norm()
# %%
x = np.arange(-3, 3.1, 0.1)
# %%
x
# %%
plt.plot(x, normal.pdf(x))
plt.show()
# %%
normal.expect()
# %%
normal.interval(0.95)
# %%
normal.pdf(0)
# %%
0.8413447460685429
# %%
plt.plot(x, normal.cdf(x))
# %%
normal.cdf(-1)
# %%
plt.plot(x, normal.pdf(x))
plt.show()
# %%
normal.expect()
# %%
normal.interval(0.95)
# %%
# Funcion de densidad
# Funcion de densidad acumulada
# %%
normal.pdf(0)
# %%
normal.cdf(1)
# %%
plt.plot(x, normal.cdf(x))
# %%
normal.cdf(-1)
# %%
plt.plot(x, normal.pdf(x))
plt.scatter(normal.interval(0.95), (0,0), marker='|', s=10000, c='r')
plt.show()
# %%
normal.rvs(19)
# %%
binom = stats.binom(10, 0.5)
# %%
# no es la probabilidad de sacar 5 aguilas
binom.expect()

# %%
binom.interval(0.95)
# %%
# la probabilidad de sacar 5 aguilas
binom.pmf(5)
# %%
x = np.arange(0,11,1)
plt.scatter(x, binom.pmf(x))
# %%
