import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
df = pd.read_csv('data/body_short.csv')

def run_eda_app() :
   
   df = pd.read_csv('data/body_short.csv')
   
   st.subheader('데이터에 관한 전체적인 정보를 보여줍니다.')
   if st.button ('데이터프레임') :
      st.dataframe(df)
   
   if st.button ('통계치') :
      st.dataframe(df.describe())

   st.subheader('선택한 컬럼의 정보를 보여줍니다.')
   selected_columns = st.multiselect('컬럼을 선택하세요', df.columns)
   if len(selected_columns) != 0 :
      st.dataframe(df[selected_columns])
   else :
      st.write('선택한 컬럼이 없습니다.')

   st.subheader('선택한 컬럼의 상관계수와 차트를 보여줍니다.')
   df_corr = df.iloc[ : , : -2+1 ]

   selected_corr = st.multiselect('컬럼을 선택하세요', df_corr.columns)

    # 유저가 1개라도 컬럼을 선택했을 경우
   if len(selected_corr) > 0 :
      st.dataframe(df_corr[selected_corr].corr())

        # 상관계수를 수치로도 구하고, 차트로도 표시하라.
      # fig1 = sns.pairplot(data = df_corr[selected_corr])
      # st.pyplot(fig1)

      selected_radio = st.radio('그래프를 선택하세요', ('라인차트', '아리아차트', '바차트'))    
      if selected_radio == '라인차트' :
         chart_data = pd.DataFrame(df_corr[selected_corr])

         st.line_chart(chart_data)

      elif selected_radio == '아리아차트' :
         chart_data = pd.DataFrame(df_corr[selected_corr])

         st.area_chart(chart_data)

      elif selected_radio == '바차트' :
         chart_data = pd.DataFrame(df_corr[selected_corr])

         st.bar_chart(chart_data)
    # 유저가 컬럼을 선택하지 않은 경우 

   else : 
      st.write('선택한 컬럼이 없습니다.')
   
   
   
   

   