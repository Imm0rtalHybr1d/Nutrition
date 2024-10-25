
import streamlit as st
from get_user_metrics import User_data 


udata: User_data = User_data()
class Calc:
    def __init__(self):
        pass
             
    def calc_BMI_BMR(self) -> None:
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
            try:
                #get TDEE
                st.session_state.user_TDEE = float(st.session_state.user_BMR * st.session_state.activity_level)
            except ValueError as e:
                st.session_state.user_TDEE = ''   
                
            udata.display_user_stats()
        except (ValueError, TypeError) as e:
            user_BMI = ''
            
    