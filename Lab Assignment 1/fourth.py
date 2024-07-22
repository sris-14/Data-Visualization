def display_words_less_than_4_characters(filename):
    try:
        with open(filename, 'r') as file:
            words = []
            for line in file:
                line_words = line.strip().split()
                words.extend([word for word in line_words if len(word) < 4])
            
            print(f"Words less than 4 characters in '{filename}':")
            for word in words:
                print(word)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


filename = "python.txt"
display_words_less_than_4_characters(filename)