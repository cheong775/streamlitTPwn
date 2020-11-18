import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from PIL import Image
import base64

data= pd.read_csv("D:/covid19_tweets.csv",encoding='ANSI',usecols =  ['user_name','user_location','user_description','user_created','user_followers','user_friends','user_favourites','user_verified','date','text','hashtags','source','is_retweet'])
st.title("Streamlit app")
st.header("this is a header")
st.subheader("this is a subheader")
st.dataframe(data)
arr = np.random.normal(1,1,size=100)
plt.hist(arr,bins=20)
plt.title("matplotlib plot")
st.pyplot()
number = st.number_input("insert a number",123)
st.write("the number is:",number)
