import numpy as np
import pickle
import streamlit as st

# Load the classifier
pickle_in = open(r"C:\Users\hrish\OneDrive\Desktop\Portfolio\Cardiovascular prediction\cardio_model.pkl", "rb")
classifier = pickle.load(pickle_in)

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

# Function to get recommendations
def get_recommendations(bmi, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active):
    recs = ["🏥 **General Tip**: Regular health checkups help catch risks early."]

    # BMI recommendations
    if bmi < 18.5:
        recs.append("🍽️ You are underweight. Consider healthy calorie intake to normalize BMI.")
    elif bmi >= 25:
        recs.append("🏃‍♂️ Aim to reduce weight through regular exercise and a balanced diet.")

    # Blood pressure
    if ap_hi >= 130 or ap_lo >= 85:
        recs.append("🧂 Consider reducing salt intake to manage high blood pressure.")
    
    # Cholesterol
    if cholesterol > 1:
        recs.append("🥑 Avoid trans fats, and eat more fiber to manage cholesterol levels.")

    # Glucose
    if gluc > 1:
        recs.append("🍬 Avoid sugar-rich foods and monitor glucose levels regularly.")

    # Lifestyle
    if smoke == 1:
        recs.append("🚭 Quitting smoking can significantly reduce cardiovascular risk.")
    if alco == 1:
        recs.append("🍷 Reduce alcohol intake for better heart health.")
    if active == 0:
        recs.append("🤸 Try exercising at least 3 times per week.")

    return recs

# Main app function
def main():
    st.title("Cardiovascular Disease Prediction")

    st.markdown("""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Will you have cardiovascular diseases?</h2>
    </div>
    """, unsafe_allow_html=True)

    age = st.slider("Age", 1, 100, 45)
    gender = st.selectbox("Gender", options=['Male', 'Female'])
    weight = st.slider("Weight (kg)", 30, 200, 70)
    height = st.slider("Height (cm)", 100, 220, 170)
    ap_hi = st.slider("Systolic BP", 70, 200, 120)
    ap_lo = st.slider("Diastolic BP", 40, 150, 80)
    chol = st.selectbox("Cholesterol", ['Normal', 'Above normal', 'Well above normal'])
    gluc = st.selectbox("Glucose", ['Normal', 'Above normal', 'Well above normal'])
    smoke = st.selectbox("Are you a smoker?", ['No', 'Yes'])
    alco = st.selectbox("Do you drink alcohol?", ['No', 'Yes'])
    active = st.selectbox("Do you exercise ≥ 3 times/week?", ['Yes', 'No'])

    # Convert inputs
    gender = 1 if gender == 'Male' else 0
    cholesterol = {'Normal': 1, 'Above normal': 2, 'Well above normal': 3}[chol]
    gluc = {'Normal': 1, 'Above normal': 2, 'Well above normal': 3}[gluc]
    smoke = 1 if smoke == 'Yes' else 0
    alco = 1 if alco == 'Yes' else 0
    active = 1 if active == 'Yes' else 0

    result = ""
    if st.button("Predict"):
        prediction = classifier.predict([[age, gender, height, weight, ap_hi, ap_lo,
                                          cholesterol, gluc, smoke, alco, active]])
        bmi = calculate_bmi(weight, height)

        if prediction[0] == 0:
            st.success('🎉 You are unlikely to have cardiovascular disease.')
        else:
            st.warning('⚠️ You may be at risk for cardiovascular disease.')

        # Show metrics
        st.markdown("### 📊 Health Metrics")
        st.metric("BMI", f"{bmi:.1f}", "Underweight" if bmi < 18.5 else "Normal" if bmi < 25 else "Overweight" if bmi < 30 else "Obese")
        st.metric("Blood Pressure", f"{ap_hi}/{ap_lo} mmHg")
        st.metric("Cholesterol Level", chol)
        st.metric("Glucose Level", gluc)

        # Show recommendations
        st.markdown("### ✅ Personalized Health Tips")
        for r in get_recommendations(bmi, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active):
            st.write(f"- {r}")

    if st.button("About"):
        st.info("Developed using Streamlit")

    # Sidebar Information
    st.sidebar.title("About This Tool")
    st.sidebar.info("""
This cardiovascular risk assessment tool uses machine learning to estimate your risk based on:
- Demographic factors
- Clinical measurements
- Lifestyle indicators

**Note**: Results are statistical estimates and should be interpreted by a healthcare professional.
""")
    st.sidebar.title("Health Resources")
    st.sidebar.markdown("""
- [American Heart Association](https://www.heart.org)
- [CDC Heart Disease Information](https://www.cdc.gov/heartdisease/)
- [Blood Pressure Guidelines](https://www.heart.org/en/health-topics/high-blood-pressure)
""")
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
**Created by:** Hrishit Madhavi 
**Version:** 1.0  
© 2025 All Rights Reserved
""")

if __name__ == '__main__':
    main()
