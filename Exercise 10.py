def even_or_odd(number):
    """Determine if a number is even or odd and return a message."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))

    # Call the function and store the result
    result = even_or_odd(num)

    # Print the message returned by the function
    print(result)


if __name__ == "__main__":
    main()
