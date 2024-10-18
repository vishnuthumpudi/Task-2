import json
import requests
import datetime
import time
import streamlit as st

def process_weather_data(data):
    main = data['weather'][0]['main']
    temp = kelvin_to_celsius(data['main']['temp'])
    feels_like = kelvin_to_celsius(data['main']['feels_like'])
    return main, temp, feels_like

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fetch_data(city_name,time_interval,threshold_limit):
    city = city_name.lower()
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9b59c79f8875a8cac84044b2a080bf0d"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            main, temp, feels_like = process_weather_data(data)
            st.subheader(f"Current Weather in {city_name}")
            st.write(f"**Main:** {main}")
            st.write(f"**Temperature:** {temp:.2f}°C")
            st.write(f"**Feels Like:** {feels_like:.2f}°C")
            st.write("Last Fetched: ",datetime.datetime.now())

def main():
    st.set_page_config(page_title="Real-Time Weather Data",page_icon="🧊",layout="wide",initial_sidebar_state="expanded")
    st.markdown("# Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates")
    st.divider()
    st.header("Want to know more about the application?")
    lst = ["Imagine having the power to monitor weather conditions in real-time and instantly access key insights without sifting through endless data streams.",
    "This project brings that vision to life by developing a cutting-edge system that transforms live weather data into concise, actionable insights.",
    "Using the OpenWeatherMap API, we’ll tap into real-time data on temperature, wind speed, humidity, and more.",
    "Through smart rollups and data aggregates, this system condenses complex information into quick, easy-to-understand summaries, ensuring you're always a step ahead of changing weather patterns.",
    "Whether it's for everyday decisions or strategic planning, this weather insight engine keeps you informed with up-to-the-minute, summarized forecasts."]
    s = ""
    for i in lst:
        s += "- " + i + "\n"
    st.markdown(s)
    st.divider()
    city_name = st.text_input("Country Name",placeholder="Please enter city name here")
    slider_value = st.slider("Set data refresh interval (minutes)", min_value=1, max_value=10, value=1,step = 1)
    threshold_temp = st.number_input("Temperature threshold for alerts (°C)", value=35.0)
    button = st.button("Fetch Data")
    if city_name:
        if button:
            i = 0
            while i < 2:
                fetch_data(city_name,slider_value,threshold_temp)
                time.sleep(slider_value*6)
                i += 1
            
    else:
        st.warning('Please provide a city name', icon="⚠️")


if __name__ == '__main__':
    main()