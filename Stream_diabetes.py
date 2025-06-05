import pickle
import streamlit as st


try:
    diabetes_model = pickle.load(open('random_forest_model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: 'random_forest_model.pkl' not found. Pastikan file model ada di direktori yang benar.")
    st.stop()

st.title('📊Klasifikasi Diabetes')

if 'Pregnancies_val' not in st.session_state:
    st.session_state.Pregnancies_val = ''
if 'Glucose_val' not in st.session_state:
    st.session_state.Glucose_val = ''
if 'BloodPressure_val' not in st.session_state:
    st.session_state.BloodPressure_val = ''
if 'SkinThickness_val' not in st.session_state:
    st.session_state.SkinThickness_val = ''
if 'Insulin_val' not in st.session_state:
    st.session_state.Insulin_val = ''
if 'BMI_val' not in st.session_state:
    st.session_state.BMI_val = ''
if 'DiabetesPedigreeFunction_val' not in st.session_state:
    st.session_state.DiabetesPedigreeFunction_val = ''
if 'Age_val' not in st.session_state:
    st.session_state.Age_val = ''


col1, col2 = st.columns(2)
with col1 :
    Pregnancies = st.text_input(
        ' Pregnancies',
        value=st.session_state.Pregnancies_val,
        key='input_pregnancies', 
        on_change=lambda: st.session_state.__setitem__('Pregnancies_val', st.session_state.input_pregnancies)
    )

with col2 :
    Glucose = st.text_input(
        ' Glucose',
        value=st.session_state.Glucose_val,
        key='input_glucose',
        on_change=lambda: st.session_state.__setitem__('Glucose_val', st.session_state.input_glucose)
    )

with col1 :
    BloodPressure = st.text_input(
        ' Blood Pressure',
        value=st.session_state.BloodPressure_val,
        key='input_bloodpressure',
        on_change=lambda: st.session_state.__setitem__('BloodPressure_val', st.session_state.input_bloodpressure)
    )

with col2 :
    SkinThickness = st.text_input(
        ' Skin Thickness',
        value=st.session_state.SkinThickness_val,
        key='input_skinthickness',
        on_change=lambda: st.session_state.__setitem__('SkinThickness_val', st.session_state.input_skinthickness)
    )

with col1 :
    Insulin = st.text_input(
        ' Insulin',
        value=st.session_state.Insulin_val,
        key='input_insulin',
        on_change=lambda: st.session_state.__setitem__('Insulin_val', st.session_state.input_insulin)
    )

with col2 :
    BMI = st.text_input(
        ' BMI',
        value=st.session_state.BMI_val,
        key='input_bmi',
        on_change=lambda: st.session_state.__setitem__('BMI_val', st.session_state.input_bmi)
    )

with col1 :
    DiabetesPedigreeFunction = st.text_input(
        ' Diabetes Pedigree Function',
        value=st.session_state.DiabetesPedigreeFunction_val,
        key='input_dpf',
        on_change=lambda: st.session_state.__setitem__('DiabetesPedigreeFunction_val', st.session_state.input_dpf)
    )

with col2 :
    Age = st.text_input(
        ' Age',
        value=st.session_state.Age_val,
        key='input_age',
        on_change=lambda: st.session_state.__setitem__('Age_val', st.session_state.input_age)
    )



col1, col2, _ = st.columns([2, 1, 4.5])
with col1:
    test_button = st.button('Test Prediksi Diabetes')

with col2:
    reset_button = st.button('Reset')
    
def to_float(value):
    return float(value.replace(',', '.'))

diab_diagnosis = ''

if test_button:
    try:
        
        input_data = [[
            to_float(Pregnancies), to_float(Glucose), to_float(BloodPressure),
            to_float(SkinThickness), to_float(Insulin), to_float(BMI),
            to_float(DiabetesPedigreeFunction), to_float(Age)
        ]]

        diab_prediction = diabetes_model.predict(input_data)

        if(diab_prediction[0] == 1):
            diab_diagnosis = 'Pasien terkena Diabetes'
        else:
            diab_diagnosis = 'Pasien tidak terkena Diabetes'

    except ValueError:
        diab_diagnosis = 'Harap masukkan semua input angka yang valid (gunakan koma atau titik).'
    except Exception as e:
        diab_diagnosis = f'Terjadi kesalahan: {e}'
        
st.success(diab_diagnosis)


if reset_button:
    
    st.session_state.Pregnancies_val = ''
    st.session_state.Glucose_val = ''
    st.session_state.BloodPressure_val = ''
    st.session_state.SkinThickness_val = ''
    st.session_state.Insulin_val = ''
    st.session_state.BMI_val = ''
    st.session_state.DiabetesPedigreeFunction_val = ''
    st.session_state.Age_val = ''
    st.rerun() 