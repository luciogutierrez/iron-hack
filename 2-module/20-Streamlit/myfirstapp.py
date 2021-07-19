import streamlit as st
import pandas as pd
import numpy as np

from sklearn import tree
from sklearn.model_selection import train_test_split

# Cargar datasets
df = pd.read_csv(income.csv)

st.write(df.columns)
st.image(pig.jpg)

siteHeader = st.beta_container()
with siteHeader:
    #Titulo
    st.title('Modelo de Evaluación de ingresos')
    st.markdown("""
                **El objetivo de este proyecto** es proveer una herramenta
                para publicar los laboratorios para que queden en la nube
                """)

dataExploration = st.beta_container()
with dataExploration:
    st.header('Data Exploration')
    st.subheader("""
                **texto 2
                """)
    st.text('Para el desarrollo de este proyecto utilizaremos una trasfromación del siguiente set de datos')
    st.dataframe(df.head())

dataViz = st.beta_container()
with dataViz:
    st.subheader('Exploration de datos')
    st.text('Distribución de datos por sexo')
    st.area_chart(df.sex.value_counts())
    st.bar_chart(df.age.value_counts())

newFeatures = st.beta_container()
with newFeatures:
    st.subheader('Selección de variables')
    st.markdown("de manera inicial, el moddelo tarbaja con las variales **race, sex, workclass y education**")
    st.text('Quieres considerar alguna otra variable?')

optional_cols = ['education-num','marital-status','occupation','relationship']
options = st.multiselect('Variables que se añadirán al modelo:', optional_cols)

principal_columns = ['race','sex','workclass','education']
drop_columns = ['income','fnlwgt','capital-gain','capital-loss','native-country','income_bi']

if len(options) != 0:
    principal_columns += options
    drop_columns += [i for i in optional_cols if i not in options]
else:
    drop_columns += optional_cols

modelTraining = st.beta_container()

with modelTraining:
    st.subheader('Entrenamiento de modelo')
    st.text('En esta sección puedes seleccioanr los parametros del modelo')

# Definimos nuestras Variables
y = df['income_bi']
df = df.drop(drop_columns, axis=1)
X = pd.get_dummies(df, columns=principal_columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=15)

max_depth = st.slider('¿Cual debería se el valor de max_deph para el modelo?', min_value=1, max_value=10, value=7, step=1)

#Modelo
t = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth = max_depth)
model = t.fit(X_train, y_train)

# performance del modelo
score_train = model.score(X_train, y_train)
score_test = model.score(X_test, y_test)

Performance = st.beta_container()
with Performance:
    st.subheader('Performance del modelo')
    col1, col2 = st.beta_columns(2)
    with col1:
        st.text('Score Train')
        st.text(round(score_train*100, 1))
    with col2:
        st.text('Score Test')
        st.text(round(score_train*100, 2))



