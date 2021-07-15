
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title = 'streamlit sample dashboard template',
    page_icon = '🎢',
    layout = 'wide'
    
)

st.markdown('## KPI Firt Row')


kpi1, kpi2, kpi3 = st.beta_columns(3)


with kpi1:
    st.markdown('**Frist KPI**')
    number1 = 111
    st.markdown(f"<h1 style='text-align:center; color:red;'>{number1}</h1>", unsafe_allow_html=True)
    

with kpi2:
    st.markdown('**Second KPI**')
    number2 = 222
    st.markdown(f"<h1 style='text-align:center; color:red;'>{number2}</h1>", unsafe_allow_html=True)


with kpi3:
    st.markdown('**Third KPI**')
    number3 = 333
    st.markdown(f"<h1 style='text-align:center; color:red;'>{number3}</h1>", unsafe_allow_html=True)


st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown("## KPI Second Row")
kpi01, kpi02, kpi03, kpi04, kpi05 = st.beta_columns(5)


with kpi01:
    st.markdown('**Another 1st KPI**')
    number1 = 111
    st.markdown(f"<h1 style='text-align:center; color:yellow;'>{number1}</h1>", unsafe_allow_html=True)
with kpi02:
    st.markdown('**Another 1st KPI**')
    number2 = 222
    st.markdown(f"<h1 style='text-align:center; color:yellow;'>{number2}</h1>", unsafe_allow_html=True)
with kpi03:
    st.markdown('**Another 1st KPI**')
    number3 = 333
    st.markdown(f"<h1 style='text-align:center; color:yellow;'>{number3}</h1>", unsafe_allow_html=True)
with kpi04:
    st.markdown('**Another 1st KPI**')
    number4 = 444
    st.markdown(f"<h1 style='text-align:center; color:yellow;'>{number4}</h1>", unsafe_allow_html=True)
with kpi05:
    st.markdown('**Another 1st KPI**')
    number5 = 555
    st.markdown(f"<h1 style='text-align:center; color:yellow;'>{number5}</h1>", unsafe_allow_html=True)


st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown("## Chart Layout")

chart1, chart2 = st.beta_columns(2)

with chart1:
    chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
    st.line_chart(chart_data)

with chart2:
    chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
    st.bar_chart(chart_data)


