def count_uppercase_characters(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            count = sum(1 for char in content if char.isupper())
            print(f"Total number of uppercase characters in '{filename}': {count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


filename = "python.txt"
count_uppercase_characters(filename)
