import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app() :
    st.subheader('데이터 분석')
    df = pd.read_csv('data/body_short.csv')

    st.dataframe(df)

    st.subheader('Nan 데이터 확인')

    st.dataframe(df.isna().sum())

    st.subheader('각 컬럼별 히스토그램 확인')

    selected_columns = st.selectbox('컬럼을 선택하세요', df.columns)

    sns.pairplot(data=df, vars=['age', 'gender', 'height_cm', 'weight_kg', 'diastolic', 'systolic',
       'sit_ups_counts'], hue='class')
    plt.show()

    sns.countplot(data=df, x='class')
    plt.show()

    plt.figure(figsize=(20,10))
    sns.heatmap(data=df.corr(),annot=True, fmt='.1f', cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5)



    st.subheader('각 컬럼별 통계치')
    st.dataframe(df.describe())