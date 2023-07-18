import streamlit as st
import pickle

st.title('Used Car Price Prediction')
st.subheader("Get an estimated value of the car")

with st.form("Form", clear_on_submit=True):
    car = st.text_input("Car name")
    brandName = car.split(" ")[0].title()
    modelName = " ".join(car.split(" ")[1:3]).title()
        
    Years = [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010,
            2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999,
            1998, 1997, 1996, 1995, 1992]
    year = st.selectbox("Year of purchase", Years, index=0)

    kms = st.number_input("Kms driven", max_value=172500)
    fuel = st.selectbox("Fuel type", ["Choose type", "Petrol","LPG", "Electric", "Diesel", "CNG"])
    seller = st.selectbox("Seller type", ["Dealer", "Individual", "Trustmark Dealer"])
    transmission = st.selectbox("Transmission type", ["Manual", "Automatic"])
    owner = st.selectbox("Owner type", ["First Owner", "Second Owner", "other"])
        
    state = st.form_submit_button("Predict")

model_test_data = [[brandName, modelName, year, kms, fuel, seller, transmission, owner]]

mlModel = pickle.load(open('modelPipe.pkl', 'rb'))
pred = mlModel.predict(model_test_data)

if state:
        st.write("The estimated value for your vehicle is:")
        st.write(pred[0])
