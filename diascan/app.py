import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler, LabelEncoder, OneHotEncoder
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def load_data():
    df = pd.read_csv('merged_dataset.csv')
    return df

def train_model(df):
    features = ['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack',
                'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost',
                'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income']
    X = df[features]
    y = df['Outcome']
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def main():
    df = load_data()
    model = train_model(df)

    st.title("Diabetes Risk Prediction")
    st.write("Enter the required information to predict the risk of diabetes.")

    high_bp = st.selectbox("High Blood Pressure", [0, 1])
    high_chol = st.selectbox("High Cholesterol", [0, 1])
    chol_check = st.selectbox("Cholesterol Check", [0, 1])
    bmi = st.number_input("BMI", min_value=0.0)
    smoker = st.selectbox("Smoker", [0, 1])
    stroke = st.selectbox("Stroke", [0, 1])
    heart_disease = st.selectbox("Heart Disease/Attack", [0, 1])
    physical_activity = st.selectbox("Physical Activity", [0, 1])
    fruits = st.number_input("Fruits Intake", min_value=0)
    veggies = st.number_input("Vegetables Intake", min_value=0)
    heavy_alcohol = st.selectbox("Heavy Alcohol Consumption", [0, 1])
    healthcare = st.selectbox("Any Healthcare", [0, 1])
    no_doc_cost = st.selectbox("No Doctor Visit Due to Cost", [0, 1])
    gen_health = st.slider("General Health (1-5)", 1, 5, 3)
    mental_health = st.slider("Mental Health (1-30)", 0, 30, 15)
    phys_health = st.slider("Physical Health (1-30)", 0, 30, 15)
    diff_walk = st.slider("Difficulty Walking (1-1)", 0, 1, 0)
    sex = st.selectbox("Sex", [0, 1])
    age = st.number_input("Age", min_value=0)
    education = st.number_input("Education (Years)", min_value=0)
    income = st.number_input("Income", min_value=0)

    input_data = np.array([high_bp, high_chol, chol_check, bmi, smoker, stroke, heart_disease,
                          physical_activity, fruits, veggies, heavy_alcohol, healthcare, no_doc_cost,
                          gen_health, mental_health, phys_health, diff_walk, sex, age, education, income]).reshape(1, -1)
    prediction = model.predict(input_data)[0]
    # Displaying the prediction

    if prediction == 0:
            st.success('Congratulations! Based on the information you provided, it seems like you do not have diabetes.')
        else:
            st.error('Sorry, based on the information you provided, it seems like you may have diabetes. We recommend consulting with a healthcare professional to discuss your options.')

     #submitted = st.form_submit_button("Is diabetic ?")
    
     #if submitted:    



if __name__ == "__main__":
    main()
