# Global variables for conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    try:
        # Prompt user for temperature and unit
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            # Convert Fahrenheit to Celsius
            celsius_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius_temp:.2f}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            fahrenheit_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit_temp:.2f}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

    except ValueError as e:
        print(f"Error: {e}. Please enter a valid numeric temperature and unit.")

if __name__ == "__main__":
    main()

