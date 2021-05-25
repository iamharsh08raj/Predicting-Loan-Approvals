import pickle
import streamlit as st
import sklearn
import math
model=pickle.load(open('model.pkl','rb'))

NBClassifier=pickle.load(open('NBClassifier_model.pkl','rb'))

def Submit(num):
    if num<=0.5:
        st.error(
            'You Are Not Eligible For This Loan'
        )
    else:
        st.success(
            'Congratulations! You Got The Loan'
        )


def main():
    st.image('Loan.jpeg', width=400)
    st.title("Loan Application Dashboard")
    html_temp="""
    <div style="background-color:#002855 ; padding:10px">
    <h2 style="color:white;text-align:center;">Submit Your Details Here</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    activities=['Logistic Regression','Naive Bayes']
    option=st.sidebar.selectbox('Which Algorithm/Model Would You Like To Use?',activities)
    st.subheader(option)
    st.spinner("Hello")
    Gender_display = ('Female', 'Male')
    Gender_options = list(range(len(Gender_display)))
    Gender = st.radio("Gender", Gender_options, format_func=lambda x: Gender_display[x])
    Married_display = ('Unmarried', 'Married')
    Married_options = list(range(len(Married_display)))
    Married = st.radio("Marital Status", Married_options, format_func=lambda x: Married_display[x])
    Dependents_display = ('0', '1', '2', '3 or 3+')
    Dependents_options = list(range(len(Dependents_display)))
    Dependents = st.selectbox("Dependents", Dependents_options, format_func=lambda x: Dependents_display[x])
    Education_display = ('Non Graduate', 'Graduate')
    Education_options = list(range(len(Education_display)))
    Education = st.radio("Education", Education_options, format_func=lambda x: Education_display[x])
    Self_Employed_display = ('Employed', 'Self Employed')
    Self_Employed_options = list(range(len(Self_Employed_display)))
    Self_Employed = st.radio("Employment Status", Self_Employed_options, format_func=lambda x: Self_Employed_display[x])
    TotalIncome=st.number_input('Select The Total Income Including Coapplicant Income',min_value=0.02)
    TotalIncome_log=math.log(TotalIncome)
    LoanAmount=st.number_input('Select The Loan Amount',min_value=0.02)
    LoanAmount_log = math.log(LoanAmount)
    Loan_Amount_Term=st.slider('Select Your Loan Term In Months',min_value=6.0,max_value=480.0,step=6.0,value=12.0)
    Credit_History_display = ('Between 300 to 500', 'Above 500')
    Credit_History_options = list(range(len(Credit_History_display)))
    Credit_History = st.selectbox("Credit Score", Credit_History_options, format_func=lambda x: Credit_History_display[x])
    Property_Area_display = ('Rural', 'Semi-Urban', 'Urban')
    Property_Area_options = list(range(len(Property_Area_display)))
    Property_Area = st.selectbox("Property Area", Property_Area_options, format_func=lambda x: Property_Area_display[x])
    inputs=[[Gender,Married,Dependents,Education,Self_Employed,Loan_Amount_Term,Credit_History,Property_Area,LoanAmount_log,TotalIncome_log]]
    print(inputs)
    if st.button('Submit'):
        if option=='Logistic Regression':
            st.success(classify((model.predict(inputs))))
        else:
            st.success(classify((NBClassifier.predict(inputs))))


if __name__=='__main__' :
    main()




















