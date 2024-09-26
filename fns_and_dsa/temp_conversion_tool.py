# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5   # Conversion factor from Celsius to Fahrenheit

# Check if the global conversion factors are defined correctly
def check_global_conversion_factors():
    assert FAHRENHEIT_TO_CELSIUS_FACTOR == 5 / 9, "FAHRENHEIT_TO_CELSIUS_FACTOR is not defined correctly."
    assert CELSIUS_TO_FAHRENHEIT_FACTOR == 9 / 5, "CELSIUS_TO_FAHRENHEIT_FACTOR is not defined correctly."
    print("Global conversion factors are defined correctly.")

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # Check global conversion factors
    check_global_conversion_factors()

    # User interaction
    try:
        temperature = float(input("Enter the temperature: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            # Convert from Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
        elif unit == 'F':
            # Convert from Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
