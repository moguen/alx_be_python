from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date_time = datetime.now()

    # Format the current date and time
    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted current date and time
    print(f"Current date and time: {formatted_date_time}")

def calculate_future_date():
    # Prompt user to enter number of days
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Error: Please enter a valid integer for number of days.")
        return

    # Get current date
    current_date = datetime.now().date()

    # Calculate future date
    future_date = current_date + timedelta(days=number_of_days)

    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # Print the formatted future date
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()

