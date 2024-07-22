# program that opens a file and handle FileNotFoundError exception if file does not exist

filename = "abc.txt"
try:
    with open(filename,'r') as file:
        print("File found")
except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")        