import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

st.title('')
df = pd.read_csv('train.csv')

income_filter = st.slider('choose income:', 7005.93, 179987.28, 10000)  # min, max, default 滑块


# filter by income
df = df[df.Annual_Income >= income_filter]

# filter by the occupation

# filter by payment behavior

st.subheader('Histogram of the Median House Price')
df.Credit_Score.hist(bins=30)
