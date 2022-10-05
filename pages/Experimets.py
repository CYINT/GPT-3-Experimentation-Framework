import streamlit as st
import pandas as pd
import numpy as np
from Ui import nav_page
st.set_page_config(page_title="Plotting Demo", page_icon="📈")


df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))
st.header(NameError('Newly Created DataFrame'))
st.table(df)

table = "st.table(df)"

if st.button("< Prev"):
    nav_page("Models")
# if st.button("Next >"):
#     nav_page("Ui")