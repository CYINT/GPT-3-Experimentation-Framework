import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError

st.set_page_config(page_title="Mapping Demo", page_icon="🌍")


video_file = open('nebula_6044.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)