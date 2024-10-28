def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
def temprature_conversion():
    print("Temperature Conversion")
    fahrenheit = int(input("Enter Fahrenheit degree: "))
    celsius = int(input("Enter Celsius degree: "))

    converted_celsius = fahrenheit_to_celsius(fahrenheit)
    converted_fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"{fahrenheit} degrees Fahrenheit is {converted_celsius:.2f} degrees Celsius.")
    print(f"{celsius} degrees Celsius is {converted_fahrenheit:.2f} degrees Fahrenheit.")

temprature_conversion()
