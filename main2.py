
class WeatherApp:
    def __init__(self, city_name):
        self.city = city_name

    def get_weather(self):
        # Add code to fetch weather data from an API based on the city
        print(f"Fetching weather data for {self.city}...")
        # Display the weather information
        # Example: Temperature, Humidity, Weather Conditions, etc.

if __name__ == "__main__":
    weather_app = WeatherApp("New York")
    weather_app.get_weather()
