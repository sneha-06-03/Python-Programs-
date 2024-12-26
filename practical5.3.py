"""WAP to remove the first occurence from a string"""
string = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")

modified_string = string.replace(char_to_remove, "", 1)
print(modified_string)
