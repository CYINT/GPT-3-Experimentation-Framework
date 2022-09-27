import streamlit as st 
import pandas as pd 
import graphviz as graphviz

import graphviz as graphviz
st.graphviz_chart('''
    digraph {
        Big_shark -> Tuna
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp
    }
''')






st.header('Thank you for checking')
st.write('Coming soon !!!!')

