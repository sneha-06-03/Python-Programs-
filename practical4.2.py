"""WAP if the character is a letter, print whether the letter is uppercase or lowercase """
char = input("Enter a character: ")
if char.isalpha():
    if char.isupper():
        print("The letter is uppercase.")
    else:
        print("The letter is lowercase.")
else:
    print("The input is not a letter.")
