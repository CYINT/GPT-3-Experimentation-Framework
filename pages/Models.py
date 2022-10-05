import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from Ui import nav_page

st.set_page_config(page_title="Mapping Demo")
#from pages.Experimets import table

video_file = open('nebula_6044.mp4', 'rb')
video_bytes = video_file.read()


st.title("Making a button")
df = st.button("Click Here")
#st.write(table)
st.video(video_bytes)



if st.button("Exploration"):
    nav_page("Experimets")

