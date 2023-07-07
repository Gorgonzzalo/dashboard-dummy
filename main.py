import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data for solar power plant
solar_data = {
    'Date': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05'],
    'Power Output (kW)': [500, 520, 510, 480, 490],
    'Temperature (°C)': [30, 32, 29, 31, 28],
    'Humidity (%)': [60, 55, 58, 62, 59]
}

# Sample data for wind farm
wind_data = {
    'Date': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05'],
    'Power Output (kW)': [1000, 980, 1020, 990, 1010],
    'Wind Speed (m/s)': [5.8, 6.2, 6.5, 5.5, 6.0],
    'Temperature (°C)': [25, 23, 24, 26, 27]
}

# Create dataframes for solar power plant and wind farm
solar_df = pd.DataFrame(solar_data)
wind_df = pd.DataFrame(wind_data)

# Set page title
st.set_page_config(page_title='Power Plant Dashboard')

# Sidebar
st.sidebar.title('Dashboard Menu')
selected_page = st.sidebar.selectbox('Select a power plant', ['Solar Power Plant', 'Wind Farm'])

# Solar Power Plant page
if selected_page == 'Solar Power Plant':
    st.title('Solar Power Plant Data')
    st.write('Here is the data for the solar power plant:')
    st.write(solar_df)

    # Convert Power Output column to NumPy array before indexing
    indexed_array = np.array(solar_df['Power Output (kW)'])[:, None]
    #indexed_array = power_output_array[:, None]

    # Plot power output over time
    plt.figure(figsize=(8, 6))
    plt.plot(solar_df['Date'], indexed_array, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Power Output (kW)')
    plt.title('Solar Power Plant - Power Output')
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Wind Farm page
elif selected_page == 'Wind Farm':
    st.title('Wind Farm Data')
    st.write('Here is the data for the wind farm:')
    st.write(wind_df)

    # Convert Power Output column to NumPy array before indexing
    power_output_array = np.array(wind_df['Power Output (kW)'])
    indexed_array = power_output_array[:, None]

    # Plot power output over time
    plt.figure(figsize=(8, 6))
    plt.plot(wind_df['Date'], indexed_array, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Power Output (kW)')
    plt.title('Wind Farm - Power Output')
    plt.xticks(rotation=45)
    st.pyplot(plt)

# About page
st.sidebar.title('About')
st.sidebar.info('This is a dummy power plant dashboard.')
