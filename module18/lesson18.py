import pandas as pd
import streamlit as st

st.header('Displaying dataframe')

df = pd.DataFrame  ({
    'Name': ['Alice', 'Michael', 'Andy'],
    'Age' : [25, 32, 29],
    "City": ["nyc", "miami", "london"]
})

df

