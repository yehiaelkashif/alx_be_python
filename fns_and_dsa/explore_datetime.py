# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the current date and time
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    # Prompt the user for the number of days
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date
    future_date = datetime.now() + timedelta(days=number_of_days)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the future date
    print("Future Date after adding", number_of_days, "days:", formatted_future_date)

if __name__ == "__main__":
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Calculate a future date
    calculate_future_date()
