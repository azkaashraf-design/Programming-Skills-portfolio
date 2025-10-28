# Get user input for each piece of information
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

# Validate and convert age to an integer
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():  # ensures only numeric input is accepted
        age = int(age_input)
        break
    else:
        print("Please enter a valid number for your age.")

# Store information in a dictionary
person_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print all values on separate lines using one print() statement
print(f"{person_info['name']}\n{person_info['hometown']}\n{person_info['age']}")

