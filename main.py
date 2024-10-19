import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/image.png")
with col2:
    st.title("Kenneth Lybech")
    content = """
    Hello. I am Kenneth! I am a Python programmer. I am selfeducated through courses on udemy and selfstudy.
    I am new to Python coding. Feel free to contact me!
    """
    st.write(content)