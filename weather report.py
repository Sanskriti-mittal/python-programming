def get_weather_report(temperature):
    # Complete this function
    if temperature<22:
        result="Cold"
    elif temperature<35:
        result="Warm"
    else:
        result="Hot"
    return(result)
temperature = int(input())
# Call the get_weather_report function
result=get_weather_report(temperature)
print(result)