import streamlit as st
import pandas as pd

view = [100,150,30]

st.write('# Youtube view')
st.write('## Youtube view')
view
st.write('## bar chart')
st.bar_chart(view)
sview = pd.Series(view)
sview