import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="获取数据"
)

uploaded_file = st.file_uploader("选择需要分析的文件 .csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

