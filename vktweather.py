import project
city = input("Enter the city of your choice here")
weather_data = project.get_weather(city)
print(weather_data)
