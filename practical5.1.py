"""WAP to find the frequency of character in a string"""
string = input("Enter a string: ")
for char in set(string):  
    print(f"Character: {char}, Frequency: {string.count(char)}")
