import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Create dataframes for solar power plant and wind farm in June and July
solar_df_june = pd.DataFrame(solar_data_june)
wind_df_june = pd.DataFrame(wind_data_june)

solar_df_july = pd.DataFrame(solar_data_july)
wind_df_july = pd.DataFrame(wind_data_july)

# Set page title
st.set_page_config(page_title='Power Plant Dashboard')

# Sidebar
st.sidebar.title('Dashboard Menu')
selected_month = st.sidebar.selectbox('Select a month', ['June', 'July'])

# Solar Power Plant page
if selected_month == 'June':
    st.title('Solar Power Plant Data - June')
    st.write('Here is the data for the solar power plant in June:')
    st.write(solar_df_june)

    # Plot power output over time
    plt.figure(figsize=(8, 6))
    plt.plot(solar_df_june['Date'], solar_df_june['Power Output (kW)'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Power Output (kW)')
    plt.title('Solar Power Plant - Power Output (June)')
    plt.xticks(rotation=45)
    st.pyplot(plt)

elif selected_month == 'July':
    st.title('Solar Power Plant Data - July')
    st.write('Here is the data for the solar power plant in July:')
    st.write(solar_df_july)

    # Plot power output over time
    plt.figure(figsize=(8, 6))
    plt.plot(solar_df_july['Date'], solar_df_july['Power Output (kW)'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Power Output (kW)')
    plt.title('Solar Power Plant - Power Output (July)')
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Wind Farm page
if selected_month == 'June':
    st.title('Wind Farm Data - June')
    st.write('Here is the data for the wind farm in June:')
    st.write(wind_df_june)

    # Plot power output over time
    plt.figure(figsize=(8, 6))
    plt.plot(wind_df_june['Date'], wind_df_june['Power Output (kW)'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Power Output (kW)')
    plt.title('Wind Farm - Power Output (June)')
    plt.xticks(rotation=45)
    st.pyplot(plt)

elif selected_month == 'July':
    st.title('Wind Farm Data - July')
    st.write('Here is the data for the wind farm in July:')
    st.write(wind_df_july)

    # Plot power output over time
    plt.figure(figsize=(8, 6))
    plt.plot(wind_df_july['Date'], wind_df_july['Power Output (kW)'], marker='o')
```python
    plt.xlabel('Date')
    plt.ylabel('Power Output (kW)')
    plt.title('Wind Farm - Power Output (July)')
    plt.xticks(rotation=45)
    st.pyplot(plt)

# About page
st.sidebar.title('About')
st.sidebar.info('This is a dummy power plant dashboard.')
