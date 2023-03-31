# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd

# 시각화 라이브러리 설치
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def run_eda2_app():
    st.subheader("탐색적 자료 분석 페이지 2")

    # 데이터셋 불러오기
    iris_df = pd.read_csv('data/iris.csv')
    # st.dataframe(iris_df)
    
    # 메뉴 지정
    submenu = st.sidebar.selectbox("submenu", ['기술통계량', '그래프'])
    if submenu == "기술통계량":
        st.dataframe(iris_df)
        
        with st.expander("Species"):
            A = st.selectbox('Select Species', ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
            tmp_df = iris_df.loc[iris_df.species == A]
            st.table(tmp_df.head())
            #st.dataframe(result)
            
        with st.expander("기술 통계량"):
            result2 = pd.DataFrame(iris_df.describe()).transpose()
            st.dataframe(result2)

        with st.expander("타겟 분포"):
            result3 = iris_df['species'].value_counts()
            st.dataframe(result3)

    elif submenu == "그래프":
        st.subheader("Plots")
        fig1 = px.scatter(iris_df, 
                          x = 'sepal_width', 
                          y = 'sepal_length',
                          color = 'species',
                          size = 'petal_width',
                          hover_data = ['petal_length'],
                          title = "Scatter Plot"
                          )
        st.plotly_chart(fig1)

        # 레이아웃
        col1, col2 = st.columns(2)
        with col1:
            #st.subheader("col1")
            with st. expander("박스플롯 with Seaborn"):
                # Seaborn Graph
                fig, ax = plt.subplots()
                sns.boxplot(iris_df, x = 'species', y = 'sepal_length', ax = ax)
                st.pyplot(fig)
        with col2:
            #st.subheader("col2")
            with st. expander("히스토그램 with matplotlib"):
                # Matplotlib Graph
                fig, ax = plt.subplots()
                ax.hist(iris_df['sepal_length'], color = 'green')
                st.pyplot(fig)

        tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])
        with tab1:
            st.write('Tab 1')
            val_species = st.selectbox('종 선택', ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'))
            st.write('종 선택 : ', val_species)

            result = iris_df[iris_df['species'] == val_species]
            st.dataframe(result)

            fig1 = px.scatter(result, 
                              x = 'sepal_width', 
                              y = 'sepal_length',
                              size = 'petal_width',
                              hover_data = ['petal_length'])
            st.plotly_chart(fig1)
        with tab2:
            st.write('Tab 2')
            
    else:
        st.write("A BC")
