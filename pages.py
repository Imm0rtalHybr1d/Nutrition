import streamlit as st


#--page setup
Info_page = st.Page(
    page='gui.py',
    title='Info',
    default=True,
    icon=':material/info:'
)

calculation_page = st.Page(
    page='calculations.py',
    title= 'Calculate',
    icon=':material/functions:'
)

# -- Navigation setup
pg = st.navigation(pages=[Info_page,calculation_page])

# -- Run Navigation
pg.run()