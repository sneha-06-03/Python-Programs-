"""WAP to replace a character by another in a string"""
string = input("Enter a string: ")
old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")

modified_string = string.replace(old_char, new_char)

print("Modified string:", modified_string)
