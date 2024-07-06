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
    # Check for Global Variables
    assert 'FAHRENHEIT_TO_CELSIUS_FACTOR' in globals(), "Global variable FAHRENHEIT_TO_CELSIUS_FACTOR is missing."
    assert 'CELSIUS_TO_FAHRENHEIT_FACTOR' in globals(), "Global variable CELSIUS_TO_FAHRENHEIT_FACTOR is missing."

    # Check for Conversion Functions
    assert callable(convert_to_celsius), "Function convert_to_celsius is not defined."
    assert callable(convert_to_fahrenheit), "Function convert_to_fahrenheit is not defined."

    # Check for User Interaction
    try:
        # Simulate user input for testing
        import io
        import sys
        stdin_backup = sys.stdin
        sys.stdin = io.StringIO('100\nF\n')
        
        import temp_conversion_tool
        assert callable(temp_conversion_tool.main), "Function main in temp_conversion_tool.py is not defined."
        
        sys.stdin = stdin_backup
    except Exception as e:
        print(f"Error in testing user interaction: {e}")

    print("All checks passed. Script is ready.")

