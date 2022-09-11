from crawl_SQLinterface import read_to_df
import streamlit as st
import requests
import pandas as pd

st.title("Iran Resturants Analysis")
st.subheader('welcome to our project :)')

"""
### In this document we'll answer the following questions:


- What features can have a effect on the rate of cafe?
- Is the place of cafe have an impact on rating?  
- Do food quality and service quality and etc. rates have a meaningful relation with rate of the cafe?
- Does time of work affect the cafe business? 


""" 
col1, col2 = st.columns(2)

col1.subheader('Count of cafes in each city')

df = read_to_df('cafe').groupby('city').count().cafe_id.rename('Count')
df = df.sort_values(ascending=False)
df.index = [x.title() for x in df.index]
col1.dataframe(df)


col2.subheader('Plotting ')
col2.line_chart(df)

'''
click on [link](https://github.com/Mmli081/Iran-restaurant-analyzer/tree/develop) to access our project on github

hope you enjoy it...
'''
