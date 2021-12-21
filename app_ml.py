import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import joblib

def run_ml_app():
    classifier = joblib.load('data/best_classifier_body.pkl')
    scaler_X = joblib.load('data/scaler_X_body_short.pkl')

    st.subheader('데이터를 입력하면 운동능력을 평가합니다.')
    #age,gender,height_cm,weight_kg,diastolic,systolic,sit_ups_counts,class

    Age = st.number_input('나이를 입력하세요', min_value= 0) 

    # select_gender = st.radio('성별을 선택하세요', ('남자', '여자'))
    # if select_gender == '남자':
    #     select_gender = 1 
    # elif select_gender == '여자':
    #     select_gender = 0
    select_gender = st.radio('성별을 선택하세요.', ('남성', '여성'))
    if select_gender == '남성' :
        select_gender = 1
    elif select_gender == '여성' :
        select_gender = 0
    height_cm = st.number_input('키를 입력하세요 (146~187cm)', min_value= 0) 
    weight_kg = st.number_input('몸무게를 입력하세요 (39~108kg)', min_value= 0) 
    diastolic = st.number_input('분당 심박수를 입력하세요 (8~117번)', min_value= 0)
    systolic = st.number_input('평균 혈압을 입력하세요 (77~193mmHG)', min_value= 0)
    sit_ups_counts = st.number_input('1분 동안 가능한 윗몸일으키기 횟수를 입력하세요 (0~68개)', min_value= 0)

    if st.button('결과보기') :
        
        # 인공지능에 집어넣을 때는 넘파이 어레이!
        new_data = np.array([Age,select_gender,height_cm,weight_kg,diastolic,systolic,sit_ups_counts]) 

        new_data = new_data.reshape(1, 7)

        new_data = scaler_X.transform(new_data)

        y_pred = classifier.predict(new_data)


        st.write('당신의 신체능력은 {} 클래스 입니다.'.format(y_pred))
        # if y_pred['A'] == 'A' :
        #     st.write('당신의 신체능력은 A입니다.')

        # elif y_pred['B'] == 'B' :
        #     st.write('당신의 신체능력은 B입니다.')

        # elif y_pred['C'] == 'C' :
        #     st.write('당신의 신체능력은 C입니다.')

        # else :
        #     st.write('당신의 신체능력은 D입니다.')