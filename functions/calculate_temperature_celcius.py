def temp_celcius(temp_fahrenheit):
    calculate_temp_celcius = (float(temp_fahrenheit) - 32) * 0.5556
    return calculate_temp_celcius

def main():
    temp_in_celcius = temp_celcius(80)
    print("Temperature in celcius is:", temp_in_celcius)

main()
    