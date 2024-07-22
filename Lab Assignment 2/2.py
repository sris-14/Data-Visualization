# program that prompts the user to input an integer and raises a ValueError exception 
# if the input is not valid integer

def get_integer():
    try:
        user_input = input("Enter an integer")
        user_integer = int(user_input)
        print(f"You entered the integer: {user_integer}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the function to prompt the user
get_integer()