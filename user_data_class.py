import os
import streamlit as st

class Get_User_metrics:
    def __init__(self) -> None:
        pass

    def get_user_weight_kg(user_weight) -> float:                
        while True:
            try:
                # stores user weight in variable
                user_weight_kg :float = float(user_weight) 
                
                # Checks if user weight within range of realist weights for a person 
                if 20 <= user_weight_kg <= 635:
                    return user_weight_kg  
                else:
                    os.system('cls')
                    st.write('Please enter a valid weight ')    
                                    
            except ValueError as e:
                st.write('Please enter a valid datatype')
        
    def get_user_height_cm(self) -> float:
        while True:
            try:
                user_height_cm :float = float(input('Height in cm: '))  
                if 54 <= user_height_cm <= 256:
                    return  user_height_cm
                else:
                    os.system('cls')
                    print('Please enter a valid height')
                    
            except ValueError as e:
                os.system('cls')
                print('Please enter a valid datatype')
                
               
        
    def get_user_age(self) -> int:
        while True:
            try:
                user_age :int = int(input('Age: '))   
                if 5 <= user_age <= 100:
                    return user_age     
                else:
                    os.system('cls')
                    print('Please enter a valid age')
                    
            except ValueError as e:
                os.system('cls')
                print('Please enter a valid datatype')
                
            
        
    def get_user_gender(self) -> str:
        while True:        
            os.system('cls')    
            print('Please enter a gender, Male or Female | M or F: ')
            user_gender :str = input('Gender: ')         
            
            #ensure user enters a valid Gender       
            if user_gender.lower()  in ['male','m','M','Male', 'female','f', 'F', 'Female']:
                os.system('cls')
                return user_gender  
            else:
                os.system('cls')
                print('Please enter a  valid gender, Male or Female | M or F')
                                   
            
                  
            
            
                
        
    