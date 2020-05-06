import streamlit as st
import pandas as pd
from sklearn.externals import joblib



def main():
    
        st.title("Wine Quality Prediction APP")
        alcohol = st.slider("Alcohol",8,15)
        citric_acid = st.slider("Citric Acid",0,1)
        chlorides = st.slider("Chlorides",0.000,0.8)
        density = st.slider("Density",0.90,1.5)
        fixed_acidity = st.slider("Fixed Acidity",4,16)
        free_sulfur_dioxide = st.slider("Free Sulfur Dioxide",1,75)
        ph = st.slider("PH",0,14)
        residual_sugar = st.slider("Residual Sugar",0,16)
        sulphates = st.slider("Sulphates",0.00,2.00)
        total_sulfur_dioxide = st.slider("Total Sulfur Dioxide",0,300)
        volatile_acidity = st.slider("Volatile Acidity",0.00,5.00)


        res = pd.DataFrame(data = 
            {'alcohol':[alcohol],'citric_acid':[citric_acid],'chlorides':[chlorides],
             'density':[density],'fixed_acidity':[fixed_acidity],'free_sulfur_dioxide':[free_sulfur_dioxide],
              'ph':[ph],'residual_sugar':[residual_sugar],'sulphates':[sulphates],
              'total_sulfur_dioxide':[total_sulfur_dioxide],
              'volatile_acidity':[volatile_acidity]})

        
        model = st.selectbox("Model",["Desicion Tree","Random Forest"])
        if model == 'Desicion Tree':
                dt = joblib.load('DecisionTreeModel.pkl')
                prediction = dt.predict(res)
                
        prediction = str(prediction).strip('[]')
        if prediction == '0':
            prediction = "Bad"
        elif prediction == '1':
            prediction ="Good"
        else:
            prediction="Mid"
                    
        if st.button("Tahmin Et"):
                st.write("QUALİTY :",prediction)
                st.balloons()
    

if __name__ == '__main__':
    main()