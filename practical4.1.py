"""WAP to print whether the character is a letter or numeric digit or a special character"""
char = input("Enter a single character: ")
if char.isalpha():
    print(f"'{char}' is a letter.")
elif char.isdigit():
    print(f"'{char}' is a numeric digit.")
else:
    print(f"'{char}' is a special character.")
