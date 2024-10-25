import streamlit as st
from streamlit_extras.stylable_container import stylable_container 

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
): 
        