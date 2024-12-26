"""WAP if the character is a numeric digit, prints its name in text(e.g., if input is 9, output is NINE)"""
digit = input("Enter a digit: ")
digit_names = {
    '0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR',
    '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'
}
if digit.isdigit() and len(digit) == 1:
    print(digit_names[digit])
else:
    print("Invalid input. Please enter a single numeric digit.")
