# Write a Python program that prompts the user to input two number and raises a TypeError exception 
# if the input are not  numerical

def get_number():
    try:
        user_input1 = input("enter number1 ")
        user_input2 = input("enter number2 ")
        user_num1 = int(user_input1)
        user_num2 = int(user_input2)
        print(f"you have entered two number :{user_num1} and {user_num2}")
    except ValueError:
        print("Error: Please enter numerical values.")
    except TypeError as e:
        print(f"TypeError: {e}")

 # function to prompt the user 
get_number()        