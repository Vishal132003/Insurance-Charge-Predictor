import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('Insurance Charge Prediction')

st.write('Enter the following details to predict insurance charges:')

# Create input fields
age = st.slider('Age', 18, 65, 30)
bmi = st.number_input('BMI', 10.0, 50.0, 25.0)
smoker = st.selectbox('Smoker', ('Yes', 'No'))

# Convert smoker input to the format used in training (True/False)
smoker_yes = True if smoker == 'Yes' else False

# Add a button to trigger prediction
if st.button('Predict'):
    # Create a DataFrame from the input
    input_data = pd.DataFrame({
        'age': [age],
        'bmi': [bmi],
        'smoker_yes': [smoker_yes]
    })

    # Predict charges
    predicted_charges = model.predict(input_data)

    st.subheader('Predicted Insurance Charges:')
    st.write(f'₹{predicted_charges[0]:,.2f}')

st.code('streamlit run app.py')
