# -*- coding:utf-8 -*-
import streamlit as st
from eda_app import run_eda_app
from eda2_app import run_eda2_app

def main():
    st.markdown("Hello World")
    menu = ["Home", "탐색적 자료 분석", "머신러닝", "About", "탐색적 자료 분석 2"]
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "탐색적 자료 분석":
        run_eda_app()
    elif choice == "머신러닝":
        pass
    elif choice == "탐색적 자료 분석 2":
        run_eda2_app()
    else:
        st.subheader("About")
if __name__ == "__main__":
    main()
    