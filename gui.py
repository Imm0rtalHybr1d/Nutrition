#%% Imports
import streamlit as st
from typing import Any
import pandas as pd

from calculations import Calc

import pathlib

#-- Load CSS from the assets folder
def load_css(filepath:str) -> None:
    with open(filepath) as f:
        st.html('<button class="btn">Button</button>')
        st.html(f'<style>{f.read()}</style>')
css_path = pathlib.Path('assets/style.css')
load_css(css_path)


#-- This function reads lines from a text file containing info on BMI, BMR, and TDEE
def read_BMI_txt(starting_line:int, end_line:int=None) -> Any:
    with open(fr"BMI.txt", "r") as file:
        for i, line in enumerate(file):  
            if starting_line <= i <= end_line :
                st.write(line)

#-- Info expander
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
    
info_expander()
