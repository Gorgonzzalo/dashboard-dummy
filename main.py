import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

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

# Function to generate random ON/OFF values for outages
def generate_outages(days):
    states = ['ON', 'OFF']
    return [random.choice(states) for _ in range(days)]

# Create dataframes for solar power plant and wind farm
solar_df = pd.DataFrame(solar_data)
solar_df['Outages'] = generate_outages(len(solar_df))

wind_df = pd.DataFrame(wind_data)
wind_df['Outages'] = generate_outages(len(wind_df))

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

    # Plot power output over time
    plt.figure(figsize=(8, 6))
    plt.plot(solar_df['Date'], solar_df['Power Output (kW)'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Power Output (kW)')
    plt.title('Solar Power Plant - Power Output')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Pie chart of outage states
    outage_counts = solar_df['Outages'].value_counts()
    explode = (0.1, 0.1)
    plt.figure(figsize=(6, 6))
    plt.pie(outage_counts, labels=outage_counts.index, autopct='%1.1f%%', startangle=90, explode=explode)
    plt.title('Solar Power Plant - Outage States')
    st.pyplot(plt)

# Wind Farm page
elif selected_page == 'Wind Farm':
    st.title('Wind Farm Data')
    st.write('Here is the data for the wind farm:')
    st.write(wind_df)

    # Plot power output over time
    plt.figure(figsize=(8, 6))
    plt.plot(wind_df['Date'], wind_df['Power Output (kW)'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Power Output (kW)')
    plt.title('Wind Farm - Power Output')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Pie chart of outage states
    outage_counts = wind_df['Outages'].value_counts()
    explode = (0.1, 0.1)
    plt.figure(figsize=(6, 6))
    plt.pie(outage_counts, labels=outage_counts.index, autopct='%1.1f%%', startangle=90, explode=explode)
    plt.title('Wind Farm - Outage States')
    st.pyplot(plt)

# About page
st.sidebar.title('About')
st.sidebar.info('This is a dummy power plant dashboard.')
