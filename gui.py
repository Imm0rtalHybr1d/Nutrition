#%% Imports
import streamlit as st
from typing import Any
import pandas as pd
from streamlit_extras.stylable_container import stylable_container 
from get_user_metrics import User_data

#%% Initializing userdata class
u_data:User_data = User_data()

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

      
    
#%% Calculater Expander        
def calculator_expander() -> None:
    with st.expander('Calculate your BMI',icon=':material/calculate:'):
        metrics_col, display_stats_col = st.columns(2)
        with metrics_col:
            #calls function that creates a form and gathers user info
            user_data_form() 

        with display_stats_col:
            #calls a fucntion that calculates and displays BMI, BMR based on the stats provided in the form
            calc_BMI_BMR() 
               
#%% Create a form that promts user to enter their data
def user_data_form() -> None:
    user_metrics_form = st.form(key='User Metrics Form', clear_on_submit=False)
            
    with user_metrics_form:
        u_data.check_weight()
        u_data.check_height()        
        u_data.check_age()        
        u_data.check_gender()        
        u_data.check_activity_level()
        
        # Submit button
        # use the form data to determine BMI and TDEE and then display it  once submit button is clicked
        with stylable_container( key="button_styling",
        css_styles="""
            button {
                position: relative;
                left: 35%;
                text-align: center;
                border: none;
                height: 25px;
                color: white;
                padding: 1rem;
                transition-duration: 0.5s;
                cursor: pointer;
            }

            button:hover {
                transition: 0.5s ease-in-out;
                transform: scale(1.05);
            }
       """,
    ): st.form_submit_button('Submit')
        
        
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
        u_data.display_user_stats()
        
        
    except (ValueError, TypeError) as e:
        user_BMI = ''

     
def calc_TDEE() -> Any:
    try:
        #get TDEE
        st.session_state.user_TDEE = float(st.session_state.user_BMR * st.session_state.activity_level)
        
    except ValueError as e:
        st.session_state.user_TDEE = ''

      
def main():
    info_expander()
    calculator_expander()

               
           
#%%        
if __name__ == "__main__":
    main()
 