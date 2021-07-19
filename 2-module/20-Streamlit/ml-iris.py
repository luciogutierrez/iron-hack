import streamlit as st
import numpy as np
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

classes = {0:'setosa', 1:'versicolor', 2:'virginica'}
class_labels = list(classes.values())

st.title('Clasificación de especies de iris')
st.markdown('**Objetivo**: Dados los detalles de la flor, tratamos de predecir la especie.')
st.markdown('El modelo puede predecir si pertenece a las siguientes categorias: **setosa, versicolor, virginica**')

def predict(arr):
    # Load the model
    with open('final_model.sav', 'rb') as f:
        model = pickle.load(f)
    classes = {0:'Iris Setosa',1:'Iris Versicolor',2:'Iris Virginica'}
    # return prediction as well as class probabilities
    preds = model.predict_proba([arr])[0]
    return (classes[np.argmax(preds)], preds)

def predict_class():
    data = list(map(float,[sepal_length,sepal_width,petal_length, petal_width]))
    result, probs = predict(data)
    st.write("The predicted class is ",result)
    probs = [np.round(x,6) for x in probs]
    
    fig, ax = plt.subplots()
    ax = sns.barplot(probs ,class_labels, palette="winter", orient='h')
    ax.set_yticklabels(class_labels,rotation=0)
    plt.title("Probabilities of the Data belonging to each class")
    for index, value in enumerate(probs):
        plt.text(value, index,str(value))
    st.pyplot(fig)
    
st.markdown("**Please enter the details of the flower in the form of 4 floating point values separated by commas**")
sepal_length = st.text_input('Enter sepal_length', '')
sepal_width = st.text_input('Enter sepal_width', '')
petal_length = st.text_input('Enter petal_length', '')
petal_width = st.text_input('Enter petal_width', '')

if st.button("Predict"):
    predict_class()
