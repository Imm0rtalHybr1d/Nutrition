#%% Imports
import streamlit as st
from typing import Any
import pandas as pd
from streamlit_extras.stylable_container import stylable_container 
from get_user_metrics import User_data
from calculations import Calculations
#%% Initializations
mycalc: Calculations = Calculations()

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
    left_drop_down, right_drop_down  = st.columns([4,4])
    with left_drop_down:
        with st.expander('BMI',expanded=True, icon=':material/health_metrics:'):
            st.header('What is BMI')
            read_BMI_txt(starting_line=0, end_line=4)
    with right_drop_down:        
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
            mycalc.calc_BMI_BMR()
               
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
                background-color: #5b92eb;
                color: white;
            }
       """,
    ): st.form_submit_button('Submit')
        
  
def main():
    info_expander()
    calculator_expander()

#%%        
if __name__ == "__main__":
    main()
 