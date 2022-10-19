import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Health Coach", page_icon=":heart:", layout="wide" )

with st.container():
    st.title ("HealthCoach :heart: :running:")
    st.subheader("hey")

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
