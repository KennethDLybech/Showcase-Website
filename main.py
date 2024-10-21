import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/image.png")
with col2:
    st.title("Kenneth Lybech")
    content = """
    Hello. I am Kenneth! I am a Python programmer. I am self-educated through courses on udemy and self-study.
    I am new to Python coding. You will find all my projects below. Feel free to contact me!
    """
    st.write(content)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
