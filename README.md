# Real-Time Weather Monitoring System with Rollups and Aggregates

## Overview

This project is a real-time data processing system that monitors weather conditions across major metros in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad). It provides summarized insights using rollups and aggregates for daily weather conditions such as average, minimum, and maximum temperatures, as well as the dominant weather condition. 

Additionally, the system supports configurable alerts based on user-defined thresholds (e.g., alert when the temperature exceeds 35°C). 

The system fetches weather data from the [OpenWeatherMap API](https://openweathermap.org/), processes it, and displays the results via a user-friendly Streamlit web application. 

## Features

- **Real-Time Weather Data:** Continuously fetches weather data at user-configurable intervals for major Indian cities.
- **Daily Weather Summaries:** Aggregates weather data to calculate daily statistics (average, max, min temperature, and dominant weather condition).
- **User-Defined Alerts:** Alerts users when specific thresholds (e.g., temperature) are exceeded.
- **Customizable Settings:** Allows users to select cities, set temperature thresholds, and configure the data refresh rate.
- **Data Visualizations:** Displays trends in temperature data through interactive charts.
- **Temperature Conversion:** Supports temperature conversion from Kelvin to Celsius or Fahrenheit based on user preference.

## Technologies Used

- **Streamlit**: The web framework for building the application interface.
- **OpenWeatherMap API**: Provides the real-time weather data.
- **Pandas**: Used for data manipulation and calculation of rollups/aggregates.
- **Matplotlib/Plotly**: For visualizing weather trends (optional).
- **SQLite3** (optional): To store daily summaries for long-term analysis.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- An API key from [OpenWeatherMap](https://openweathermap.org/) (sign up for a free API key).

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-repo/weather-monitoring-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd weather-monitoring-app
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Replace `your_openweathermap_api_key` in the code with your OpenWeatherMap API key.

### Running the Application

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501/`).

### Configuration

- **City Selection**: Select the metro city from the sidebar.
- **Refresh Interval**: Set the interval (in minutes) for the application to fetch new weather data.
- **Temperature Thresholds**: Set user-defined temperature thresholds to receive alerts when these limits are exceeded.

## Usage

### Fetch Weather Data

1. Select a city from the sidebar.
2. Click on the **Fetch Weather Data** button to retrieve current weather conditions for the selected city.
3. The application will display the following information:
   - Main weather condition (e.g., Clear, Rain, Snow)
   - Current temperature (in °C)
   - Feels-like temperature (in °C)
   - Timestamp of the data update

### View Daily Summaries

- Daily weather summaries are calculated based on the weather data collected throughout the day. This includes:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition

### Set Alerts

- You can configure a temperature threshold from the sidebar. The system will trigger an alert if the current temperature exceeds this threshold for two consecutive updates.

### Visualizations

- The application displays temperature trends using line charts. This helps visualize historical temperature data throughout the day.

## Testing

You can simulate various test scenarios to ensure the system is functioning correctly:

1. **System Setup**: Ensure the application starts and connects to the OpenWeatherMap API using a valid API key.
2. **Data Retrieval**: Simulate API calls at configurable intervals to retrieve weather data for the selected location.
3. **Temperature Conversion**: Test the accuracy of temperature conversion from Kelvin to Celsius (or Fahrenheit).
4. **Daily Weather Summary**: Simulate multiple weather updates and verify the correct calculation of daily summaries.
5. **Alerting Thresholds**: Define user thresholds for temperature or weather conditions and verify that alerts are triggered when thresholds are exceeded.

## Future Enhancements

- **Additional Weather Parameters**: Extend the system to monitor more weather metrics like humidity, wind speed, and pressure.
- **Weather Forecasts**: Incorporate weather forecasts and generate summaries based on predicted conditions.
- **Email Notifications**: Add email alerting functionality when weather thresholds are exceeded.

## Contributing

Feel free to fork this project, submit issues, or make pull requests to improve the application.

## License

This project is licensed under the MIT License.

---

This README provides an overview, instructions for setup and usage, as well as potential improvements for the future.