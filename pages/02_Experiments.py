import streamlit as st 
import pandas as pd 
import numpy as np 


st.set_page_config(layout='centered', page_title='Exploration Page / Experimentation')


df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('A', 'B', 'C', 'D', 'E')

)

st.header('Sample DataFrame')


st.table(df)