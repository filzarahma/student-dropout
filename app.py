import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestClassifier

# Set page config
st.set_page_config(page_title="Student Dropout Predictor", page_icon="🎓", layout="wide")

# Load the trained model
@st.cache_resource
def load_model():
    model_path = "model/model.joblib"
    
    if os.path.isfile(model_path):
        try:
            model = joblib.load(model_path)
            return model
        except Exception as e:
            st.error(f"Failed to load model: {e}")
            return None
    else:
        st.error("Model file not found. Please train the model first.")
        return None

model = load_model()

# Helper function for mapping categorical values
def map_categorical(value, mapping_dict):
    return mapping_dict.get(value, value)

# Define the mappings (same as in notebook)
binary_map = {'Yes': 1, 'No': 0}
gender_map = {'Male': 1, 'Female': 0}

# Course mapping
course_map = {
    'Biofuel Production Technologies': 33,
    'Animation and Multimedia Design': 171,
    'Social Service (evening attendance)': 8014,
    'Agronomy': 9003,
    'Communication Design': 9070,
    'Veterinary Nursing': 9085,
    'Informatics Engineering': 9119,
    'Equinculture': 9130,
    'Management': 9147,
    'Social Service': 9238,
    'Tourism': 9254,
    'Nursing': 9500,
    'Oral Hygiene': 9556,
    'Advertising and Marketing Management': 9670,
    'Journalism and Communication': 9773,
    'Basic Education': 9853,
    'Management (evening attendance)': 9991
}

marital_status_map = {
    'Single': 1,
    'Married': 2,
    'Widower': 3,
    'Divorced': 4,
    'Facto Union': 5,
    'Legally Separated': 6
}

previous_qualification_map = {
    "Secondary education": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
    "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43
}

# Dashboard title
st.title("🎓 Student Dropout Prediction Dashboard")

st.write("""
This dashboard predicts the likelihood of student dropout based on various factors.
Enter the student information below to get a prediction.
""")

# Sidebar with info
st.sidebar.header("About")
st.sidebar.info("""
This dashboard uses a machine learning model to predict student dropout probability.

The model is based on data from over 4000 students with various academic and personal factors.

**Key predictors include:**
- Second semester academic performance
- First semester performance
- Financial status
- Age at enrollment
- Previous academic qualifications
""")

# Create form for user input
with st.form("student_data_form"):
    st.header("Student Information")
    
    # Organize inputs into columns and logical groups
    col1, col2 = st.columns(2)
    
    # Demographics and background
    with col1:
        st.subheader("Demographics")
        age = st.number_input("Age at enrollment", min_value=16, max_value=80, value=20)
        gender = st.selectbox("Gender", options=["Male", "Female"])
        marital_status = st.selectbox("Marital status", 
                                      options=list(marital_status_map.keys()))
        
        st.subheader("Academic Background")
        previous_qual = st.selectbox("Previous qualification", 
                                     options=list(previous_qualification_map.keys()))
        prev_qual_grade = st.slider("Previous qualification grade", 0.0, 200.0, 120.0, 0.1)
        course = st.selectbox("Course", options=list(course_map.keys()))
        
    # Financial and institutional details
    with col2:
        st.subheader("Financial Status")
        scholarship = st.selectbox("Scholarship holder", options=["Yes", "No"])
        debtor = st.selectbox("Debtor", options=["Yes", "No"])
        tuition_fees = st.selectbox("Tuition fees up to date", options=["Yes", "No"])
        
        st.subheader("Other Information")
        daytime_evening = st.selectbox("Daytime/evening attendance", options=["Daytime", "Evening"])
        displaced = st.selectbox("Displaced", options=["Yes", "No"])
        special_needs = st.selectbox("Educational special needs", options=["Yes", "No"])
        international = st.selectbox("International student", options=["Yes", "No"])

    # First semester performance
    st.subheader("First Semester Performance")
    col3, col4, col5 = st.columns(3)
    with col3:
        first_sem_enrolled = st.number_input("Units enrolled (1st sem)", min_value=0, max_value=20, value=6)
    with col4:
        first_sem_evaluations = st.number_input("Evaluations (1st sem)", min_value=0, max_value=30, value=6)
    with col5:
        first_sem_approved = st.number_input("Units approved (1st sem)", min_value=0, max_value=20, value=5)
    first_sem_grade = st.slider("Grade average (1st sem)", 0.0, 20.0, 12.0, 0.1)
    
    # Second semester performance
    st.subheader("Second Semester Performance")
    col6, col7, col8 = st.columns(3)
    with col6:
        second_sem_enrolled = st.number_input("Units enrolled (2nd sem)", min_value=0, max_value=20, value=6)
    with col7:
        second_sem_evaluations = st.number_input("Evaluations (2nd sem)", min_value=0, max_value=30, value=6)
    with col8:
        second_sem_approved = st.number_input("Units approved (2nd sem)", min_value=0, max_value=20, value=5)
    second_sem_grade = st.slider("Grade average (2nd sem)", 0.0, 20.0, 12.0, 0.1)
    
    # Economic context
    st.subheader("Economic Context")
    col9, col10, col11 = st.columns(3)
    with col9:
        unemployment = st.slider("Unemployment rate (%)", 5.0, 20.0, 12.0, 0.1)
    with col10:
        inflation = st.slider("Inflation rate (%)", -2.0, 5.0, 1.0, 0.1)
    with col11:
        gdp = st.slider("GDP", -5.0, 5.0, 0.0, 0.1)
    
    # Submit button
    submitted = st.form_submit_button("Predict Dropout Risk")

# Process the form data on submission
if submitted:
    # Map categorical variables to their numeric values
    gender_value = 1 if gender == "Male" else 0
    marital_status_value = marital_status_map[marital_status]
    course_value = course_map[course]
    previous_qual_value = previous_qualification_map[previous_qual]
    daytime_evening_value = 1 if daytime_evening == "Daytime" else 0
    scholarship_value = 1 if scholarship == "Yes" else 0
    debtor_value = 1 if debtor == "Yes" else 0
    tuition_fees_value = 1 if tuition_fees == "Yes" else 0
    displaced_value = 1 if displaced == "Yes" else 0
    special_needs_value = 1 if special_needs == "Yes" else 0
    international_value = 1 if international == "Yes" else 0
    
    # Create a dataframe with the user input
    input_data = pd.DataFrame({
        'Marital_status': [marital_status_value],
        'Course': [course_value],
        'Daytime_evening_attendance': [daytime_evening_value],
        'Previous_qualification': [previous_qual_value],
        'Previous_qualification_grade': [prev_qual_grade],
        'Nacionality': [1],  # Default value (Portuguese)
        'Mothers_qualification': [19],  # Default value
        'Fathers_qualification': [19],  # Default value
        'Mothers_occupation': [9],  # Default value 
        'Fathers_occupation': [9],  # Default value
        'Displaced': [displaced_value],
        'Educational_special_needs': [special_needs_value],
        'Debtor': [debtor_value],
        'Tuition_fees_up_to_date': [tuition_fees_value],
        'Gender': [gender_value],
        'Scholarship_holder': [scholarship_value],
        'Age_at_enrollment': [age],
        'International': [international_value],
        'Curricular_units_1st_sem_credited': [0],  # Default value
        'Curricular_units_1st_sem_enrolled': [first_sem_enrolled],
        'Curricular_units_1st_sem_evaluations': [first_sem_evaluations],
        'Curricular_units_1st_sem_approved': [first_sem_approved],
        'Curricular_units_1st_sem_grade': [first_sem_grade],
        'Curricular_units_1st_sem_without_evaluations': [0],  # Default value
        'Curricular_units_2nd_sem_credited': [0],  # Default value
        'Curricular_units_2nd_sem_enrolled': [second_sem_enrolled],
        'Curricular_units_2nd_sem_evaluations': [second_sem_evaluations],
        'Curricular_units_2nd_sem_approved': [second_sem_approved],
        'Curricular_units_2nd_sem_grade': [second_sem_grade],
        'Curricular_units_2nd_sem_without_evaluations': [0],  # Default value
        'Unemployment_rate': [unemployment],
        'Inflation_rate': [inflation],
        'GDP': [gdp]
    })
    
    # Make prediction
    if model:
        # If you have a placeholder model for now
        prediction_prob = model.predict_proba(input_data)[0][1]
        prediction = model.predict(input_data)[0]
        
        # Display prediction
        st.header("Prediction Result")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Create gauge chart for dropout probability using Streamlit metrics
            st.subheader("Dropout Probability")
            st.metric(label="", value=f"{prediction_prob:.1%}")
            
            # Add risk category
            risk_category = ""
            if prediction_prob < 0.3:
                risk_category = "Low Risk 🟢"
            elif prediction_prob < 0.7:
                risk_category = "Medium Risk 🟠"
            else:
                risk_category = "High Risk 🔴"
                
            st.subheader(f"Risk Category: {risk_category}")
        
        with col2:
            # Key factors influencing decision
            st.subheader("Key Factors")
            
            # This would require feature importance from SHAP or similar
            # For now, let's use a simplified approach based on feature importance
            # and input values
            
            factors = []
            
            # Check for key risk factors based on our model's feature importance
            if second_sem_approved < 3:
                factors.append("Very low number of approved units in second semester")
            if second_sem_grade < 10:
                factors.append("Low grade average in second semester")
            if first_sem_approved < 3:
                factors.append("Very low number of approved units in first semester")
            if tuition_fees == "No":
                factors.append("Tuition fees not up to date")
            if first_sem_grade < 10:
                factors.append("Low grade average in first semester")
            if age > 30:
                factors.append("Higher age at enrollment")
            if debtor == "Yes":
                factors.append("Student has debt")
            
            if factors:
                for i, factor in enumerate(factors[:5], 1):
                    st.write(f"{i}. {factor}")
            else:
                st.write("No significant risk factors identified.")
        
        # Recommendations
        st.subheader("Recommendations")
        
        if prediction_prob < 0.3:
            st.write("""
            - 🟢 **Low Risk**: This student shows good academic progress.
            - Regular check-ins should be sufficient.
            - Encourage continued academic performance.
            """)
        elif prediction_prob < 0.7:
            st.write("""
            - 🟠 **Medium Risk**: Consider implementing preventive measures.
            - Schedule academic counseling sessions.
            - Review course load and performance.
            - Consider additional tutoring support.
            """)
        else:
            st.write("""
            - 🔴 **High Risk**: Immediate intervention recommended.
            - Schedule urgent academic counseling.
            - Explore financial aid options if applicable.
            - Consider course load reduction if appropriate.
            - Provide mental health and wellbeing resources.
            - Develop a detailed academic improvement plan.
            """)
else:
    st.info("Fill in the form and click 'Predict Dropout Risk' to get a prediction.")
