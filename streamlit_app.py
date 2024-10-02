import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

from PIL import Image
#for displaying images

st.title("Data Science App")

image_path = Image.open('wine1.webp')
st.image(image_path, width = 600)

df = pd.read_csv('wine.csv')

st.dataframe(df.head(5))

st.subheader("01 Description of the dataset")

st.dataframe(df.describe())

st.subheader("02 Missing values")

dfnull = df.isnull()/len(df)*100
total_missing = dfnull.sum().round(2)
if total_missing[0] <0.1:
    st.success("Congrats you have no missing values")
else:
    st.write(total_missing)

st.subheader("03 Data Visualization")

list_columns = df.columns

values = st.multiselect("Select two variables: ",list_columns, ["quality", "citric acid"])

#linechart
st.line_chart(df, x = values[0], y = values[1])

#barchart
st.bar_chart(df, x = values[0], y = values[1])

#pairplot
values_pairplot = st.multiselect("Select four variables: ",list_columns, ["quality", "citric acid", "chlorides", "alcohol"])

df2 = df[[values_pairplot[0],values_pairplot[1],values_pairplot[2],values_pairplot[3]]]
pair = sns.pairplot(df2)
st.pyplot(pair)
