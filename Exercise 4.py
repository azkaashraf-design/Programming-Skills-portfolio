# Improved version: ignores capitalization

answer = input("What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct! 🎉")
else:
    print("Wrong! The correct answer is Paris.")


