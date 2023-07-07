import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

# Sample data for solar power plant in June
solar_data_june = {
    'Date': ['2023-06-01', '2023-06-02', '2023-06-03', '2023-06-04', '2023-06-05'],
    'Power Output (kW)': [480, 520, 510, 500, 490],
    'Temperature (°C)': [28, 30, 29, 29, 28],
    'Humidity (%)': [62, 60, 58, 59, 60]
}

# Sample data for wind farm in June
wind_data_june = {
    'Date': ['2023-06-01', '2023-06-02', '2023-06-03', '2023-06-04', '2023-06-05'],
    'Power Output (kW)': [980, 1000, 1020, 1010, 990],
    'Wind Speed (m/s)': [5.5, 6.0, 6.2, 6.1, 5.8],
    'Temperature (°C)': [23, 24, 24, 25, 23]
}

# Sample data for solar power plant in July
solar_data_july = {
    'Date': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05'],
    'Power Output (kW)': [500, 520, 510, 480, 490],
    'Temperature (°C)': [30, 32, 29, 31, 28],
    'Humidity (%)': [60, 55, 58, 62, 59]
}

# Sample data for wind farm in July
wind_data_july = {
    'Date': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05'],
    'Power Output (kW)': [1000, 980, 1020, 990, 1010],
    'Wind Speed (m/s)': [5.8, 6.2, 6.5, 5.5, 6.0],
    'Temperature (°C)': [25, 23, 24, 26, 27]
}

# Function to generate random ON/OFF values for outages
def generate_outages(days):
    states = ['ON', 'OFF']
    return [random.choice(states) for _ in range(days)]

# Create dataframes for solar power plant and wind farm in June and July
solar_df_june = pd.DataFrame(solar_data_june)
solar_df_june['Outages'] = generate_outages(len(solar_df_june))

wind_df_june = pd.DataFrame(wind_data_june)
wind_df_june['Outages'] = generate_outages(len(wind_df_june))

solar_df_july = pd.DataFrame(solar_data_july)
solar_df_july['Outages'] = generate_outages(len(solar_df_july))

wind_df_july = pd.DataFrame(wind_data_july)
wind_df_july['Outages'] = generate_outages(len(wind_df_july))

# Set page title
st.set_page_config(page_title='Power Plant Dashboard')

# Sidebar
st.sidebar.title('Dashboard Menu')
selected_power_plant = st.sidebar.selectbox('Select a power plant', ['Solar Power Plant', 'Wind Farm'])

# Solar Power Plant page
if selected_power_plant == 'Solar Power Plant':
    st.title('Solar Power Plant Data')

    # Dropdown menu to select the month
    selected_month_solar = st.selectbox('Select a month', ['June', 'July'])

    if selected_month_solar == 'June':
        st.write('Here is the data for the solar power plant in June:')

        # Layout for power output plot and pie chart
        col1, col2 = st.beta_columns([2, 1])

        # Power output plot
        with col1:
            plt.figure(figsize=(8, 6))
            plt.plot(solar_df_june['Date'], solar_df_june['Power Output (kW)'], marker='o')
            plt.xlabel('Date')
            plt.ylabel('Power Output (kW)')
            plt.title('Solar Power Plant - Power Output (June)')
            plt.xticks(rotation=45)
            st.pyplot(plt)

        # Pie chart of outage states
        with col2:
            outage_counts = solar_df_june['Outages'].value_counts()
            explode = (0.1, 0.1)
            plt.figure(figsize=(6, 6))
            plt.pie(outage_counts, labels=outage_counts.index, autopct='%1.1f%%', startangle=90, explode=explode)
            plt.title('Solar Power Plant - Outage States (June)')
            st.pyplot(plt)

    elif selected_month_solar == 'July':
        st.write('Here is the data for the solar power plant in July:')

        # Layout for power output plot and pie chart
        col1, col2 = st.beta_columns([2, 1])

        # Power output plot
        with col1:
            plt.figure(figsize=(8, 6))
            plt.plot(solar_df_july['Date'], solar_df_july['Power Output (kW)'], marker='o')
            plt.xlabel('Date')
            plt.ylabel('Power Output (kW)')
            plt.title('Solar Power Plant - Power Output (July)')
            plt.xticks(rotation=45)
            st.pyplot(plt)

        # Pie chart of outage states
        with col2:
            outage_counts = solar_df_july['Outages'].value_counts()
            explode = (0.1, 0.1)
            plt.figure(figsize=(6, 6))
            plt.pie(outage_counts, labels=outage_counts.index, autopct='%1.1f%%', startangle=90, explode=explode)
            plt.title('Solar Power Plant - Outage States (July)')
            st.pyplot(plt)

# Wind Farm page
elif selected_power_plant == 'Wind Farm':
    st.title('Wind Farm Data')

    # Dropdown menu to select the month
    selected_month_wind = st.selectbox('Select a month', ['June', 'July'])

    if selected_month_wind == 'June':
        st.write('Here is the data for the wind farm in June:')

        # Layout for power output plot and pie chart
        col1, col2 = st.beta_columns([2, 1])

        # Power output plot
        with col1:
            plt.figure(figsize=(8, 6))
            plt.plot(wind_df_june['Date'], wind_df_june['Power Output (kW)'], marker='o')
            plt.xlabel('Date')
            plt.ylabel('Power Output (kW)')
            plt.title('Wind Farm - Power Output (June)')
            plt.xticks(rotation=45)
            st.pyplot(plt)

        # Pie chart of outage states
        with col2:
            outage_counts = wind_df_june['Outages'].value_counts()
            explode = (0.1, 0.1)
            plt.figure(figsize=(6, 6))
            plt.pie(outage_counts, labels=outage_counts.index, autopct='%1.1f%%', startangle=90, explode=explode)
            plt.title('Wind Farm - Outage States (June)')
            st.pyplot(plt)

    elif selected_month_wind == 'July':
        st.write('Here is the data for the wind farm in July:')

        # Layout for power output plot and pie chart
        col1, col2 = st.beta_columns([2, 1])

        # Power output plot
        with col1:
            plt.figure(figsize=(8, 6))
            plt.plot(wind_df_july['Date'], wind_df_july['Power Output (kW)'], marker='o')
            plt.xlabel('Date')
            plt.ylabel('Power Output (kW)')
            plt.title('Wind Farm - Power Output (July)')
            plt.xticks(rotation=45)
            st.pyplot(plt)

        # Pie chart of outage states
        with col2:
            outage_counts = wind_df_july['Outages'].value_counts()
            explode = (0.1, 0.1)
            plt.figure(figsize=(6, 6))
            plt.pie(outage_counts, labels=outage_counts.index, autopct='%1.1f%%', startangle=90, explode=explode)
            plt.title('Wind Farm - Outage States (July)')
            st.pyplot(plt)

# About page
st.sidebar.title('About')
st.sidebar.info('This is a dummy power plant dashboard.')
