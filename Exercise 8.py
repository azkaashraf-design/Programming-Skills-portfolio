# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user for a name to search
search_name = input("Enter a name to search for: ").strip()

# Check if the name exists in the list (case-sensitive)
if search_name in names:
    print(f"{search_name} was found in the list! ✅")
else:
    print(f"{search_name} was not found in the list. ❌")
