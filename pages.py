import streamlit as st


#--page setup
Info_page = st.Page(
    page='gui.py',
    title='Info',
    default=True
)

calculation_page = st.Page(
    page='calculations.py',
    title= 'Calculate'
)

# -- Navigation setup
pg = st.navigation(pages=[Info_page,calculation_page])

# -- Run Navigation
pg.run()