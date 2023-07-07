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
df = pd.DataFrame(data)

# Sidebar
st.sidebar.title('Dashboard Menu')
selected_page = st.sidebar.selectbox('Select a page', ['Home', 'Data'])

# Home page
if selected_page == 'Home':
    st.title('Welcome to the Dummy Dashboard!')
    st.write('This is the home page of the dashboard.')

# Data page
elif selected_page == 'Data':
    st.title('Data')
    st.write('Here is some example data:')
    st.dataframe(df)

# About page
st.sidebar.title('About')
st.sidebar.info('This is a dummy dashboard created using Streamlit.')

