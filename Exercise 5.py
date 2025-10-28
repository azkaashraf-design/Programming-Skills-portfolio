# Dictionary mapping month numbers to days
days_in_month = {
    1: 31,
    2: 28,  # Default for February
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user for the month number
month = int(input("Enter the month number (1-12): "))

if month in days_in_month:
    # Special handling for February (month 2)
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").strip().lower()
        if leap == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        print(f"Month {month} has {days_in_month[month]} days.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
