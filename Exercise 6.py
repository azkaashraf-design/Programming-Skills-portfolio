# Define the correct password
correct_password = "12345"

# Maximum number of attempts allowed
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("Access granted! ✅")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) left.")
        else:
            print("Too many failed attempts! Authorities have been alerted. 🚨")

