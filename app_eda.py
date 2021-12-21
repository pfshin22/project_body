import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


def run_eda_app() :
   
   df = pd.read_csv('data/body_short.csv')
   
   st.subheader('데이터에 관한 정보를 보여줍니다.')
   if st.button ('데이터프레임') :
      st.dataframe(df)
   
   if st.button ('통계치') :
      st.dataframe(df.describe())

   st.subheader('각 데이터의 관계를 파악하기 위한 시각적 표현')
   selected_radio = st.radio('그래프를 선택하세요', ('라인차트', '아리아차트', '바차트'))    
   if selected_radio == '라인차트' :
      chart_data = pd.DataFrame(
         np.random.randn(20, 2),
         columns=['age', 'gender'])

      st.line_chart(chart_data)

   elif selected_radio == '아리아차트' :
      chart_data = pd.DataFrame(
         np.random.randn(20, 2),
         columns=['age', 'gender'])

      st.area_chart(chart_data)

   elif selected_radio == '바차트' :
      chart_data = pd.DataFrame(
         np.random.randn(50, 2),
         columns=['age', 'gender'])

      st.bar_chart(chart_data)

   