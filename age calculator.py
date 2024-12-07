from datetime import datetime

# Function to calculate age
def calculate_age():
    # Get the user's birthdate
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

    try:
        # Convert the birthdate string to a datetime object
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

        # Get the current date
        current_date = datetime.now()

        # Calculate the difference in years
        age = current_date.year - birthdate.year

        # Adjust the age if the birthday hasn't occurred yet this year
        if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
            age -= 1

        # Display the result
        print(f"You are {age} years old.")

    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Run the age calculator
calculate_age()
