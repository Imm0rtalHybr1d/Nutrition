#%% Imports
import streamlit as st
from typing import Any
import pandas as pd
from streamlit_extras.stylable_container import stylable_container 
from genAI import Gen_AI

#%% This function reads lines from a text file containing info on BMI, BMR, and TDEE
def read_BMI_txt(starting_line:int, end_line:int=None) -> Any:
    with open(fr"BMI.txt", "r") as file:
        
        for i, line in enumerate(file):  
            if starting_line <= i <= end_line  :
                st.write(line)


#%% Info expander
def info_expander() -> None:
    test1, test2  = st.columns([4,4])
    with test1:
        with st.expander('BMI',expanded=True, icon=':material/health_metrics:'):
            st.header('What is BMI')
            read_BMI_txt(starting_line=0, end_line=4)
    with test2:        
        with st.expander('BMR',expanded=True,icon=':material/outpatient_med:'):
            st.header('What is BMR')
            read_BMI_txt(starting_line=5, end_line=8)
    with st.expander('TDEE'):
        st.header('What is TDEE')
        read_BMI_txt(starting_line=9, end_line=10)

def css_btn():
    # this funtion defines the style of the AI button 
    #with stylable allows us to use CSS to style certain elements, in this case its a button called ai_btn
    with stylable_container( key="button_styling",
        css_styles="""
            button {
                border: none;
                color: white;
                padding: 16px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                transition-duration: 0.4s;
                cursor: pointer;
            }

            button {
                background-color: white; 
                color: black; 
                border: 2px solid #04AA6D;
            }

            button:hover {
                background-color: #C45A6D;
                color: white;
            }
       """,
    ):
        
        ai_btn = st.button("Ask AI", key='ai_btn',type='secondary')
        if ai_btn:
            myai: Gen_AI = Gen_AI()
            
            st.write(myai.get_ai_response(prompt='if someones BMI is 26.3, their BMR is 1564.45 and their TDEE is 2424.89, what can you advise if this persons gaol is to lose weight'))
            st.write('AI button has been clicked ')
        

    
#%% Calculater Expander        
# 
def calculator_expander() -> None:

    with st.expander('Calculate your BMI',icon=':material/calculate:'):
        metrics_col, display_stats_col = st.columns(2)
        
        with metrics_col:
            #calls function that creates a form and gathers user info
            user_data_form() 

        with display_stats_col:
            #calls a fucntion that calculates and displays BMI, BMR based on the stats provided in the form
            calc_BMI_BMR() 
            
#%% Get user metrics from text_input within form
def check_weight() -> None:
    # ensure user enters a float value for weight
    try:
        user_weight:float = float(st.text_input(label='Enter your weight in kg:'))
        st.session_state.user_weight  = user_weight
        return  True
        
    except Exception as e:
        st.session_state.user_weight  = ''
        
def check_height() -> None:
    try:
        user_height:float = float(st.text_input(label='Enter your height in cm:'))
        st.session_state.user_height_in_CM = user_height
        
    except Exception as e:
        st.session_state.user_height_in_CM = ''
     
def check_age() -> None:
    try:
        check_age:float = float(st.text_input(label='Enter your Age:'))
        st.session_state.user_age = check_age
        
    except Exception as e:
        st.session_state.user_age = ''
         
def check_gender() -> None:
    try:        
        user_gender:str = st.selectbox('Gender', ['Male', 'Female'])        
        
        if user_gender.lower() == 'male' or user_gender.lower() == 'female':
            st.session_state.user_gender = user_gender            
        else:
            st.session_state.user_gender = ''
    except Exception as e :
        st.session_state.user_gender = ''
 
def check_activity_level() -> None:
    try:
        activity_level = st.selectbox("Activity level", ["Not active", "Lightly active",'Moderately active','Very active','Extremely active'])
        
        if activity_level == 'Not active':
            st.session_state.selected_activity_level = 'Not active'
            st.session_state.activity_level = 1.2
            
        elif activity_level == 'Lightly active':
            st.session_state.selected_activity_level = 'Lightly active'
            st.session_state.activity_level = 1.375  
            
        elif activity_level == 'Moderately active':
            st.session_state.selected_activity_level = 'Moderately active'
            st.session_state.activity_level = 1.55 
            
        elif activity_level == 'Very active':
            st.session_state.selected_activity_level = 'Very active'
            st.session_state.activity_level = 1.725  
            
        else:
            st.session_state.selected_activity_level = 'Extremely active'
            st.session_state.activity_level = 1.9  
    except Exception as e:
        st.session_state.activity_level = ''
            
               
#%% Create a form that promts user to enter their data
def user_data_form() -> None:
    user_metrics_form = st.form(key='User Metrics Form', clear_on_submit=False)
            
    with user_metrics_form:
        check_weight()
        check_height()
        check_age()
        check_gender()
        check_activity_level()
        
        # Submit button
        # use the form data to determin BMI and TDEE and then display it 
        submit_btn = st.form_submit_button('Submit')
        if submit_btn:            
            try:
                st.write(f"""A {round(st.session_state.user_age)} year old {st.session_state.user_gender} 
                        that weighs {st.session_state.user_weight}kg and is {st.session_state.user_height_in_CM}cm tall, 
                        that is {st.session_state.selected_activity_level}""")
            except TypeError as e:
                st.write('')
#%% BMI calculation             
def calc_BMI_BMR() -> None:
    try:
        #get BMI
        user_BMI: float = st.session_state.user_weight / (st.session_state.user_height_in_CM/100) ** 2       
        
        #set BMI in session state
        st.session_state.user_BMI = round(user_BMI,2)
        
        # Get BMR and Adjust based on gender
        if st.session_state.user_gender == 'male':
            st.session_state.user_BMR = float(88.362 + (13.397 * st.session_state.user_weight ) + (4.799 * st.session_state.user_height_in_CM) - (5.677 * st.session_state.user_age))
        else:
            st.session_state.user_BMR = float(447.593 + (9.247 * st.session_state.user_weight ) + (3.098 * st.session_state.user_height_in_CM) - (4.330 *  st.session_state.user_age))
        
        #get TDEE
        calc_TDEE()
        display_user_stats()
        
        
    except (ValueError, TypeError) as e:
        user_BMI = ''
        
def display_user_stats() -> None:
    #display user stats
        st.subheader(f'Your Stats:')
        st.markdown('#### =========================')  
        st.markdown(f'##### BMI: {st.session_state.user_BMI}')
        st.markdown(f'##### BMR: {st.session_state.user_BMR:.2f}') 
        st.markdown(f'##### TDEE: {st.session_state.user_TDEE:.2F}') 
     
def calc_TDEE() -> Any:
    try:
        #get TDEE
        st.session_state.user_TDEE = float(st.session_state.user_BMR * st.session_state.activity_level)
        
    except ValueError as e:
        st.session_state.user_TDEE = ''

      
def main():
    
    info_expander()
    calculator_expander()

    sidebar1 = st.sidebar
    with sidebar1:
        css_btn()             
           
#%%        
if __name__ == "__main__":
    main()
 