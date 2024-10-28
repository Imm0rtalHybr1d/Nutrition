import streamlit as st
import time

class Calc:
    def __init__(self):
        pass
    
    def check_weight(self) -> None:
    # ensure user enters a float value for weight
        try:
            user_weight:float = float(st.text_input(label='Enter your weight in kg:'))
            st.session_state.user_weight  = user_weight
        except ValueError as e:
            st.session_state.user_weight  = '' 
            
        
    def check_height(self) -> None:
        try:
            user_height:float = float(st.text_input(label='Enter your height in cm:'))
            st.session_state.user_height_in_CM = user_height
             
        except Exception as e:
            st.session_state.user_height_in_CM = ''
    
    def check_age(self) -> None:
        try:
            check_age:float = float(st.text_input(label='Enter your Age:'))
            st.session_state.user_age = check_age
             
        except Exception as e:
            st.session_state.user_age = ''  
    
    def check_gender(self) -> None:
        try:        
            user_gender:str = st.selectbox('Gender', ['Male', 'Female'])        
            
            if user_gender.lower() == 'male' or user_gender.lower() == 'female':
                st.session_state.user_gender = user_gender 
                     
            else:
                st.session_state.user_gender = ''
        except Exception as e :
            st.session_state.user_gender = ''    
    
    def check_activity_level(self) -> None:
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
    
    def calc_BMI(self) -> None:
        try:
            # -- Get BMI
            user_BMI: float = st.session_state.user_weight / (st.session_state.user_height_in_CM/100) ** 2                   
            #set BMI in session state
            st.session_state.user_BMI = float( round(user_BMI,2))
        except (ValueError, AttributeError) as e:
            st.session_state.user_BMI = ''
          
    def calc_BMR(self) -> None:
        try:      
            # Get BMR and Adjust based on gender
            if st.session_state.user_gender == 'male':
                st.session_state.user_BMR = 88.362 + (13.397 * st.session_state.user_weight ) + (4.799 * st.session_state.user_height_in_CM) - (5.677 * st.session_state.user_age)
                
            else:
                st.session_state.user_BMR = float(447.593 + (9.247 * st.session_state.user_weight ) + (3.098 * st.session_state.user_height_in_CM) - (4.330 *  st.session_state.user_age))
                
        except (ValueError, AttributeError) as e:
            st.session_state.user_BMR = ' '
      
    def calc_TDEE(self) -> None:
        #-- Get TDEE
        try:
            st.session_state.user_TDEE = float(st.session_state.user_BMR * st.session_state.activity_level)
            
        except ValueError :
            st.session_state.user_TDEE = ' ' 
          
def user_data_form() -> bool:
    user_metrics_form = st.form(key='User Metrics Form', clear_on_submit=False)
    mycalc: Calc = Calc()     
         
    with user_metrics_form:
        #-- Get and set user metrics
        mycalc.check_weight()
        mycalc.check_height()        
        mycalc.check_age()        
        mycalc.check_gender()        
        mycalc.check_activity_level()
        
        #-- If submit button is clicked then try calculating BMI,BMR and TDEE    
        submit_btn = st.form_submit_button(label='Submit')
        if submit_btn:
            #-- if user hasnt filled in the form and still tried to submit, display a message indicating to fill in fields
            try:
                mycalc.calc_BMI()
                mycalc.calc_BMR()
                mycalc.calc_TDEE()
            #-- Calculating BMI, BMR and TDEE with missing values will always result in an exception, therefore we use try-catch and display error message    
            except (TypeError, AttributeError) : 
                st.error('Do not leave any blank spaces, fill in all the fields with the correct format')  
            else:
                st.success(body='Data submitted')
                return True
                # st.write(st.session_state.user_BMI)
                # st.write(st.session_state.user_BMR)
                # st.write(st.session_state.user_TDEE)
                
expander = st.expander(label='Calcualte your BMI, BMR & TDEE', expanded=True)
with expander:
    left_col, right_col = st.columns(2)
    # user_data_form()
    with left_col:
        if user_data_form() == True:
            
            st.write(st.session_state.user_BMI)
            st.write(st.session_state.user_BMR)
            st.write(st.session_state.user_TDEE)
    
    