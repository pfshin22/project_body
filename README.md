### project_body
# 주제 : 유저가 입력한 신체조건 항목값을 종합하여, 인공지능으로 등급을 분류하기
### • 기획 : 유저의 신체조건 (성별, 키, 몸무게, 심박수, 혈압, 윗몸일으키기 횟수 등)를 입력하면 A~D 4개의 등급으로 분류
### • 설계 : 사람들의 신체조건들과 등급을 인공지능(머신러닝)으로 정규화하여 분류할 수 있도록 모델링하고, vscode와 streamlit을 활용하여 웹으로 참여할 수 있도록 구현.
### • 데이터정리, 인공지능 학습 : 
1. 조사한 빅데이터 데이터프레임을 코랩에서 import, 등급을 y변수로, 나머지 조건들의 데이터를 x변수로 설정. 
2. X범위가 각각 다르기 때문에 X를 sklern의 StandardScaler로 정규화
3. X와 y를 학습, 테스트 변수로 분리
4. SVM Classifrier로 모델링 
5. 모델평가 : X테스트를 예측하고 confusion matrix로 검증
6. 다른 커널 사용 : SVC의 파라미터로 kernel = 'rbf'로 설정해서 머신러닝
7. 학습한 모델을 joblib을 이용하여 pkl파일로 생성

### vscode를 이용해 웹 대시보드 구성 : 메인화면(app.py), 데이터정보, 인공지능 적용 3개의 페이지로 구성
### • 데이터정보: 
1. 전체적인 데이터프레임과 describe정보를 출력
2. 판다스, matplotlib, seaborn, aitair를 이용하여 선택한 컬럼 데이터간의 상관계수를 라인, 바, 아리아 차트로 시각화

### • 인공지능 적용 : 
1. joblib을 이용해 학습시킨 모델을 load
2. 유저가 입력해야 하는 항목들을 슬라이더, 라디오, number_input등을 활용하여 구성
3. np.array를 사용해서 학습된 인공지능에 데이터값 입력하여 적용
4. value값 2차원으로 reshape, 
5. value값 scaler하고, 예측
6. inverse_transform으로 원래 단위로 환산하여 출력

