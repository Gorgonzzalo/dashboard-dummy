import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title='Dummy Dashboard')

# Create some example data
data = {
    'Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Age': [25, 30, 35, 40],
    'Gender': ['Male', 'Female', 'Male', 'Female']
}
dfCartuja = pd.DataFrame(data)
data2 = {
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [1, 2, 3, 4],
    'Gender': ['ON', 'OFF', 'OFF', 'ON']
}
dfPicon = pd.DataFrame(data2)

# Sidebar
st.sidebar.title('Dashboard Menu')
selected_page = st.sidebar.selectbox('Select a Project', ['Home', 'Picón', 'Cartuja'])

# Home page
if selected_page == 'Home':
    st.title('Welcome to the ABEI Dummy Dashboard!')
    st.write('This is the home page of the dashboard.')

# Data page
elif selected_page == 'Picón':
    st.title('Picón Dashboard')
    st.write('Here is some example data:')
    st.dataframe(dfPicon)
elif selected_page == 'Cartuja':
    st.title('Cartuja Dashboard')
    st.write('Here is some example data:')
    st.dataframe(dfCartuja)
# About page
st.sidebar.title('About')
st.sidebar.info('This is a dummy dashboard created using Streamlit.')

