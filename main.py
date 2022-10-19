import entrypoint as entrypoint
import streamlit as st
import pandas as pd
import numpy as np
from numpy.core.setup_common import file

st.title ("HealthCoach")

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.run [entrypoint file]