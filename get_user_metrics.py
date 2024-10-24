import streamlit as st

class User_data:
    def __init__(self):
        pass
    
    def check_weight(self) -> None:
    # ensure user enters a float value for weight
        try:
            user_weight:float = float(st.text_input(label='Enter your weight in kg:'))
            st.session_state.user_weight  = user_weight
            return  True
        except Exception as e:
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
            
    def display_user_stats(self) -> None:
    #display user stats
        st.subheader(f'Your Stats:')
        st.markdown('#### =========================')  
        st.markdown(f'##### BMI: {st.session_state.user_BMI}')
        st.markdown(f'##### BMR: {st.session_state.user_BMR:.2f}') 
        st.markdown(f'##### TDEE: {st.session_state.user_TDEE:.2F}')         