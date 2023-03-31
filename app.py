# -*- coding:utf-8 -*-
import streamlit as st
from eda_app import run_eda_app
from eda2_app import run_eda2_app
from PIL import Image
from ml_app import run_ml_app

def main():
    st.markdown("Hello World")
    menu = ["Home", "탐색적 자료 분석", "머신러닝", "About", "탐색적 자료 분석 2"]
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == "Home":
        img = Image.open('data\iris.jpg')
        st.subheader("Home")
        st.image(img)
    elif choice == "탐색적 자료 분석":
        run_eda_app()
    elif choice == "머신러닝":
         run_ml_app()
    elif choice == "탐색적 자료 분석 2":
        run_eda2_app()
    else:
        st.subheader("About")
if __name__ == "__main__":
    main()
    