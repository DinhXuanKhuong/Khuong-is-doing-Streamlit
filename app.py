import streamlit as st
import numpy as np
import pandas as pd 
import altair as alt


st.header("Hello, welcome to my streamlit website")
st.write("This is the project showing my journey of 30 days of Streamlit")
st.subheader("This is a subheader", divider = True)
st.caption("This is an caption")

df = pd.DataFrame({"Name": ["Dinh Xuan Khuong"], "Age": [21], "Email": ["dinhxuankhuong2005@gmail.com"]})

st.write("You can also display a dataframe like below", df)

st.write("How about a chart?")
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)