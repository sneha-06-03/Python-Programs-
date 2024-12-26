""" WAP to read a file and (a) Print the total number of characters, words and lines in the file, (b) Calculate the frequency of each character in the file. Use a variable of dictionary type to maintain the count, (c) Print the words in reverse order."""

filename = "your_file.txt"  
try:
    with open(filename, 'r') as file:
        text = file.read()

        # Total number of characters, words, and lines
        num_characters = len(text)
        num_words = len(text.split())
        num_lines = text.count('\n') + 1  # Counting lines

        print(f"Total characters: {num_characters}")
        print(f"Total words: {num_words}")
        print(f"Total lines: {num_lines}")

        # Calculate frequency of each character using a dictionary
        char_frequency = {}
        for char in text:
            char_frequency[char] = char_frequency.get(char, 0) + 1
        
        print("Character frequencies:")
        for char, freq in char_frequency.items():
            print(f"'{char}': {freq}")

        # Print words in reverse order
        words = text.split()
        reversed_words = ' '.join(reversed(words))
        print("\nWords in reverse order:")
        print(reversed_words)

except FileNotFoundError:
    print(f"The file {filename} does not exist.")
