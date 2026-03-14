def main():
    temperature_celcius = float(input("Enter your temperature in celcius: "))
    
    temperature_fahrenheit = (temperature_celcius * (9 / 5)) + 32.0
    
    temperature_kelvin = temperature_celcius + 273.15
    
    print(f"The temperature is: \n{temperature_celcius} °C\n{temperature_fahrenheit} °F\n{temperature_kelvin} K")

main()