#%%
import time
# from genAI import Gen_AI
from typing import Any
import os
from dataclasses import dataclass, field
import user_data_class
import streamlit as st

os.system('cls')
#%% Defining Dataclass
@dataclass
class user_metrics:    
    user_weight_kg:float
    user_height_cm:float
    user_age :int
    user_active_level:str = field(init=False)
    user_gender:str 
    
 #%%   Calculates BMI
    def calc_BMI(self) -> dict|Any:
            
        user_BMI: float = self.user_weight_kg / (self.user_height_cm / 100) ** 2
        user_BMI: float = round(user_BMI, 2)
        
        if user_BMI < 18.5:
            return {user_BMI: 'Interpretation: Underweight'}
        elif 18.5 <= user_BMI < 25:
            return {user_BMI: 'Interpretation: Normal weight'}
        elif 25 <= user_BMI < 30:
            return {user_BMI: 'Interpretation: Overweight'}
        else:
            return {user_BMI: 'Interpretation: Obese'}
 
 #%% Calculate TDEE
    def calc_TDEE(self) -> float:

        activity_level:dict[str,str] = {1:'Sedentary', 
                                        2:'Lightly active', 
                                        3:'Moderately active', 
                                        4:'Very active', 
                                        5:'Extremely active', }     
        
        if self.user_gender in ['male','m','M','Male']:
            BMR:float = 88.362 + (13.397 * self.user_weight_kg ) + (4.799 * self.user_height_cm) - (5.677 * self.user_age)
        else:
            BMR:float = 447.593 + (9.247 * self.user_weight_kg ) + (3.098 * self.user_height_cm) - (4.330 * self.user_age)
        os.system('cls')   
        print('Lets calculate your TDEE ...')
        print('')
        print('Activity level, Choose between the following options :')    
        for k, v in activity_level.items():
            print(f'{k}. {v}')
        print('')
        
        while True:
            user_active_level = input('Activity level: ')    
            
            #check user activity valid:
            actvity_lv = check_user_activity(user_active_level.strip()) 
            if not actvity_lv == False:
                TDEE:float = BMR * actvity_lv
                return TDEE
            else:
                print('Please enter a valid activity level')     
                print('Your options are: Sedentary, Lightly active, Moderately active, Very active, Extremely active')
        
#%% Activity level
def check_user_activity(user_active_level:str) -> Any:
    
    if user_active_level.lower() in ['sedentary', 'lightly active', 'moderately active', 'very active', 'extremely active']:
        match user_active_level.lower():
            case 'sedentary':
                return 1.2
            case 'lightly active':
                return 1.375
            case 'moderately active':
                return 1.55
            case 'very active':
                return 1.725
            case 'extremely active':
                return 1.9
    else:
        return False

#%% initialize dataclass
def get_user_data() -> user_metrics:
        
    get_ud: user_data_class = user_data_class.Get_User_metrics()    
    
    user_weight_kg :float = get_ud.get_user_weight_kg()
    user_height_cm :float = get_ud.get_user_height_cm()
    user_age :int = get_ud.get_user_age()
    user_gender :str = get_ud.get_user_gender()           
        
    # Initiate dataclass with all gathered data
    user: user_metrics = user_metrics(user_weight_kg, user_height_cm, user_age,  user_gender)
    return user    




#%% Reading from BMI file
def display_BMI_info(starting_line:int, end_line:int=None) -> Any:
    
    with open(fr"C:\Users\01465307\OneDrive - University of Cape Town\Desktop\Nutrition\BMI.txt", "r") as file:
        
        for i, line in enumerate(file):  
            if starting_line <= i <= end_line  :
                return line   
            
#%%       
def main():
    
    display_BMI_info(starting_line=0, end_line=5)
    time.sleep(10)
    os.system('cls')
    
    print('Lets calculate your BMI ...')
    
    my_data = get_user_data() #calls a function that returns a class object containing user data       
    final_BMI = my_data.calc_BMI() # calls a function that retreive user's BMI   
    
    os.system('cls')
    for k, v in final_BMI.items(): #displays user BMI along with info relating to BMI
        print(f'Your BMI ≈ {k}')        
    display_BMI_info(starting_line=7, end_line=18)
    time.sleep(10)
    os.system('cls')
    
    
    final_TDEE = my_data.calc_TDEE()
    os.system('cls')
    print(f'Your TDEE ≈ {final_TDEE:.2f}')    
    display_BMI_info(starting_line=19, end_line=23)
        
    prompt:str= f"""Based on the user's metrics what would you suggest from a nutrional standpoint,
                                            here are their metrics,The user age is {my_data.user_age},               
                                            their gender is {my_data.user_gender}, 
                                            their activity level is {final_TDEE},
                                            their TDEE is {final_TDEE:.2f},
                                            their Weight is {my_data.user_weight_kg},
                                            their Height is {my_data.user_height_cm},
                                            their goal is to be in a healthy weight based on the thier BMI {final_BMI.get(k)},
                                            you can decide their dietary preference for them"""

    try:
        myai: Gen_AI = Gen_AI()
        ai_response: str = myai.get_ai_response(prompt)
    except Exception as e:
        print(e)
    print(ai_response)
    
 
if __name__ == "__main__":
    main()
 

# %%