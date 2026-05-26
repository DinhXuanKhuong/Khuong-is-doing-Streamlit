import streamlit as st
import numpy as np
import pandas as pd 
import altair as alt
from datetime import time, datetime


RANDOM_SEED = 42

np.random.seed(RANDOM_SEED)


st.header("Hello, welcome to my streamlit website")
st.write("This is the project showing my journey of 30 days of Streamlit")
st.subheader("This is a subheader", divider = True)
st.caption("This is an caption")

st.subheader("Working with data", divider = True)

df = pd.DataFrame({"Name": ["Dinh Xuan Khuong"], "Age": [21], "Email": ["dinhxuankhuong2005@gmail.com"]})

st.write("You can also display a dataframe like below", df)

st.write("How about a chart?")
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.subheader("Let's learn about slider", divider = True)
st.write("You can write code like this")


code_body = """
import streamlit as st

age = st.slider("how old are you?", 0, 130, 25)

# 0, 130, 25 represent the minimum, maximum and default values, 

st.write("Im ", age, " year olds")


""".strip()

st.code(code_body , "python")

age = st.slider("how old are you?", 0, 130, 25)
st.write("Im ", age, " year olds")

st.subheader('Range slider')

values = st.slider("Select a range of values", 0.0, 100.0, (0.25, 0.75))

st.write('Values:', values)


st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30), # The default value for the datetime was set using the value option to be January 1, 2020 at 9:30
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

st.header("st.line_chart")


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


st.header('st.selectbox')

option = st.selectbox("Choose your favorite color: ", ("Blue", "Green", "Yellow"))

st.write(f"Your favorite color is: ", option)

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red']) # Default

st.write('You selected:', options)