import streamlit as st
import numpy as np
import tensorflow as tf

nav=st.sidebar.radio('Navigation Panel',['Home','About'])
st.sidebar.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 25px;
}
    </style>
    """, unsafe_allow_html=True)
if nav=='Home':
    st.header('CUSTOMER CHURN PREDICTION')
    st.markdown('<h4>ENTER THE DETAILS</h4>',unsafe_allow_html=True)
    first,last,gender=st.columns(3)
    display = ["male", "female"]
    options = list(range(len(display)))
    g = gender.selectbox("Gender", options, format_func=lambda x: display[x])
    fname=first.text_input('First Name')
    lname=last.text_input('Last Name')
    contract,sctzn,partner=st.columns(3)
    display = ['Month-to-month','One year','Two year']
    options = list(range(len(display)))
    c=contract.selectbox('How is their contract',options, format_func=lambda x: display[x])
    display = ['Yes','No']
    options = list(range(len(display)))
    s=sctzn.selectbox('Are they a Senior Citizen',options, format_func=lambda x: display[x])
    p=partner.selectbox('Do they have any partner',options, format_func=lambda x: display[x])
    phoneservice,internetservice,onlinebackup=st.columns(3)
    ps=phoneservice.selectbox('Do they have phone service',options, format_func=lambda x: display[x])
    display = ['Cable','Fiber Optic','No Service']
    options = list(range(len(display)))
    ints=internetservice.selectbox('What is their internet service type',options, format_func=lambda x: display[x])
    display = ['Yes','No','No Internet Service']
    options = list(range(len(display)))
    ob=onlinebackup.selectbox('Do they have online backup',options,format_func=lambda x: display[x])
    deviceprotection,techsupport,streamingmovies=st.columns(3)
    dp=deviceprotection.selectbox('Do they have device protection',options,format_func=lambda x: display[x])
    ts=techsupport.selectbox('Do they have tech support',options, format_func=lambda x: display[x])
    stm=streamingmovies.selectbox('Do you have streaming movies',options, format_func=lambda x: display[x])
    tenure=st.number_input('What is their tenure')
    monthlycharges=st.number_input('What is their monthly charges')
    totalcharges=st.number_input('What is their total charges')
    submit=st.button('Submit Details')
    button_style = """
        <style>
        .stButton > button {
            width: 100%;
        }
        </style>
        """
    st.markdown(button_style, unsafe_allow_html=True)
    if submit:
        loaded_model=tf.keras.models.load_model('mymodel3')
        data=np.array([g,s,p,tenure,ps,ints,ob,dp,ts,stm,c,monthlycharges,totalcharges])
        t=np.transpose(np.array(data).reshape(-1,1))
        yhat=loaded_model.predict(t)
        yhat=np.round(yhat)
        if yhat==1:
            text = f"<h4><div style='text-align: center;'>{fname} {lname} will stay with us</div></h4>"
            st.write(text, unsafe_allow_html=True)
            left_co, cent_co,last_co = st.columns(3)
            with cent_co:st.image('happy.gif')
        if yhat==0:
            text = f"<h4><div style='text-align: center;'>{fname} {lname} will leave us</div></h4>"
            st.write(text, unsafe_allow_html=True)
            left_co, cent_co,last_co = st.columns(3)
            with cent_co:st.image('sad.gif')
if nav=='About':
    st.header('About Developer')
    st.markdown("")
    st.markdown('<h5>ADITYA DAS</h5>',unsafe_allow_html=True)
    email='aditya0911das@gmail.com'
    st.markdown(f"Contact me at: [{email}](mailto:{email})")
