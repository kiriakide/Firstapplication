import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Health Coach", page_icon=":red_heart:", layout="wide" )
st.title ("HealthCoach")

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
