import streamlit as st
import imagify
import figurify
import random
from PIL import Image
from streamlit import caching
def main():
    st.title("TEST")
    n=1
    kr= st.selectbox("Want to start a test?",["Select an Option","Yes","No"])

    lis=[]
    if(kr=="Yes"):
        st.header("Question1")
        st.write("Are you able to utilize the lockdown period fruitfully?")
        n=imagify.imageify(n)
        inp=st.selectbox("",["Select an Option","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key='1')
        lis.append(inp)
        if((inp!="Select an Option")):
            st.header("Question2")
            st.write("Are you able to utilize the lockdown period fruitfully?")
            n= imagify.imageify(n)
            inp2=st.selectbox("",["Select an Option","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key='2')
            lis.append(inp2)
            if(inp2!="Select an Option"):
                st.header("Question3")
                st.write("Are you able to utilize the lockdown period fruitfully?")
                n=imagify.imageify(n)
                inp3=st.selectbox("",["Select an Option","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key='3')
                lis.append(inp3)
                if(inp3!="Select an Option"):
                    st.success("Test Completed")
                    st.write(lis)
if __name__ == "__main__":
    main()
   


